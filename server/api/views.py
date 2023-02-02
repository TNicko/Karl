from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Session
from .serializers import SessionSerializer
from scrapyd_api import ScrapydAPI
import api.gpt as gpt

def get_search_url(searchTerm: str) -> str:
    """Get search url from search term"""
    search_url = f"https://www.google.com/search?q={searchTerm}"
    return search_url

@api_view(['GET'])
def getRoutes(request):
    sessions = Session.objects.all()
    sessions_serializer = SessionSerializer(sessions, many=True)
    return Response(sessions_serializer.data)

@api_view(['POST', 'GET'])
def getSearchResults(request):

    if request.method == 'POST':
        # Get search query from client
        searchTerm = request.query_params['q']
        search_url = get_search_url(searchTerm)
        print("search url: ", search_url)

        # Custom settings for scrapy spider
        settings = {
            "USER_AGENT": "Mozilla/5.0 (compatible; Googlebot/2.1; "
            "+http://www.google.com/bot.html)",
        }

        status = 'started'
        session = Session(status=status, search_url=search_url, title=searchTerm)
        session.save()

        # Connect scrapyd service
        scrapyd = ScrapydAPI('http://scrapyd:6800/')
        
        try:
            # Schedule crawling task
            task_id = scrapyd.schedule('default', 'google_search', settings=settings, url=search_url, domain='google.com')
            session.status = 'running'
            session.task_id = task_id
            session.save()
        except Exception as e:
            session.status = 'failed'
            session.save()
            print("Error while scheduling task: ", e)
            return Response({'status': session.status})
        
        return Response({'status': session.status, 'session_id': session.id, 'task_id': task_id, 'session_id': session.id})
    
    if request.method == 'GET':
        
        task_id = request.GET.get('task_id', None)

        if not task_id:
            return Response({'error': 'task_id is missing'})
        
        # Connect scrapyd service
        scrapyd = ScrapydAPI('http://scrapyd:6800/')
        
        # Check status of crawling task
        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                session = Session.objects.get(task_id=task_id)
                session.status = status
                session.save()

                # DUMMY DATA
                message = 'This is the scraped data' 
                urls = ['https://dummyurl.com'] 
                search_data = {
                    'searchTerm': session.title,
                    'message': session.content,
                    'urls': urls,
                }
                print(session.content)
                return Response({'status': status, 'search_data': search_data})
            except Exception as e:
                return Response({'error': str(e)})
        else:
            return Response({'status': status})



        # # !!! DUMMY DATA !!!
        # urls = ['https://www.google.com/search?q=hello+world']

        # # Get response from GPT-3
        # gpt_prompt = f"Summarize what is mentioned in following link: {urls[0]}"
        # message = gpt.gpt_response(gpt_prompt)
        # message = message.strip()
        # print(message)

        # data = {
        #     'searchTerm': searchTerm,
        #     'message': message,
        #     'urls': urls,
        # }
        # return Response(data)