import React, { useState, useEffect } from 'react';
import VideoBackground from './VideoBackground';
import Logo from './Logo';
import ButtonRow from './ButtonRow';
import GridSection from './GridSection';
const Main: React.FC = () => {
  const [textIndex, setTextIndex] = useState(0);
  const textArray = ["Automated React Architecture", "Creative Web Solutions", "Innovative Design Concepts"];
  useEffect(() => {
    const interval = setInterval(() => {
      setTextIndex((prevIndex) => (prevIndex + 1) % textArray.length);
    }, 3000);
    return () => clearInterval(interval);
  }, []);
  return (
    <div>
      <VideoBackground />
      <div className="flex flex-col items-center justify-center h-screen text-white">
        <Logo />
        <h2 className="text-3xl font-bold">{textArray[textIndex]}</h2>
        <ButtonRow />
        <GridSection title="Supported frameworks" gridLayout="2x6" />
        <GridSection title="Supported UI kits" gridLayout="6x2" />
      </div>
    </div>
  );
};
export default Main;