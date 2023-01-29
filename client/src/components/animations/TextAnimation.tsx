import React, { useState, useEffect } from "react";
import styled, { keyframes } from "styled-components";

interface Props {
  message: string;
}

const TextAnimation: React.FC<Props> = ({ message }) => {
  const [animationKey, setAnimationKey] = useState(0);
  const reactArray = message.split(" ");

  useEffect(() => {
    setAnimationKey(animationKey + 1);
  }, [message]);

  return (
    <Wrapper length={reactArray.length} key={animationKey}>
      {reactArray.map((word, i) => (
        <span key={i}>{word}</span>
      ))}
    </Wrapper>
  );
};

export default TextAnimation;

const animation = keyframes`
    0% { opacity: 0; transform: translateX(0px); }
    100% { opacity: 1; transform: translateY(0px); }
`;

const Wrapper = styled.div<{ length: number }>`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;

  span {
    margin: 0 2px;
    display: inline-block;
    opacity: 0;
    animation-name: ${animation};
    animation-duration: 0.5s;
    animation-fill-mode: both;
  }

  ${({ length }) =>
    Array.from({ length })
      .map(
        (_, i) => `
    span:nth-child(${i + 1}) {
      animation-delay: ${(i + 1) * 0.08}s;
    }`
      )
      .join("")}
`;
