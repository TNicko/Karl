from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Session, WebsitePage
from .serializers import SessionSerializer, WebsitePageSerializer
from scrapyd_api import ScrapydAPI
import api.gpt as gpt

def get_search_url(searchTerm: str) -> str:
    """Get search url from search term"""
    search_url = f"https://www.google.com/search?q={searchTerm}"
    return search_url

@api_view(['GET'])
def getRoutes(request):
    # sessions = Session.objects.all()
    # sessions_serializer = SessionSerializer(sessions, many=True)
    # return Response(sessions_serializer.data)

    webpages = WebsitePage.objects.all()
    webpages_serializer = WebsitePageSerializer(webpages, many=True)
    return Response(webpages_serializer.data)

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
    
    # if request.method == 'GET':

    #     print("get request....")
        
    #     task_id = request.GET.get('task_id', None)

    #     if not task_id:
    #         return Response({'error': 'task_id is missing'})
        
    #     # Connect scrapyd service
    #     scrapyd = ScrapydAPI('http://scrapyd:6800/')
        
    #     # Check status of crawling task
    #     status = scrapyd.job_status('default', task_id)
    #     if status == 'finished':
    #         try:
    #             session = Session.objects.get(task_id=task_id)
    #             session.status = status
    #             session.save()

    #             urls = convert_to_list(session.content)

    #             print("urls: ", urls)

    #             # Get response from GPT-3
    #             gpt_prompt = f"Summarize what is mentioned in following links: {urls}"
    #             message = gpt.gpt_response(gpt_prompt)
    #             message = message.strip()

    #             search_data = {
    #                 'searchTerm': session.title,
    #                 'message': message,
    #                 'urls': urls,
    #             }
    #             return Response({'status': status, 'search_data': search_data})
    #         except Exception as e:
    #             return Response({'status': status})
    #     else:
    #         return Response({'status': status})

def convert_to_list(s: str) -> list:
    """Convert string to list
    Args: 
        s (str): string to be converted e.g. "['url1', 'url2']"
    Returns:
        list: list of urls
    """
    if s.startswith('[') and s.endswith(']'):
        s = s[1:-1]
        url_list = [url.strip().strip("'") for url in s.split(',')]
        return url_list