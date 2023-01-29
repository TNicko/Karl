import React from "react";
import styled, { keyframes } from "styled-components";

const TitleAnimation: React.FC = () => {
  const reactArray = "KARL".split("");

  return (
    <Wrapper>
      {reactArray.map((item, i) => (
        <span key={i}>{item}</span>
      ))}
    </Wrapper>
  );
};

export default TitleAnimation;

const animation = keyframes`
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
`;

const Wrapper = styled.span`
  span {
    display: inline-block;
    margin: 0 0.1em;
    opacity: 0;
    animation-name: ${animation};
    animation-duration: 1s;
    animation-timing-function: ease-in-out;
    animation-fill-mode: forwards;
  }

  ${Array.from(
    { length: 4 },
    (_, i) => `
  span:nth-child(${i + 1}) {
    animation-delay: ${(i + 1) * 0.1}s;
  }`
  ).join("")}
`;
