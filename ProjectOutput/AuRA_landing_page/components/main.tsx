import React from 'react';
import VideoBackground from './videobackground';
import Logo from './logo';
import ButtonRow from './buttonrow';
import Info from './info';
import GridSection from './gridsection';

const Main: React.FC = () => {
  return (
    <div>
    <div style={{zIndex:'1'}}>
    <div className="video-background" style={{zIndex:'1'}}>
      <video autoPlay muted loop className="w-full h-full object-cover fixed opacity-20" style={{zIndex:'-1'}}>
        <source src="bgvideo.mp4" type="video/mp4" />
      </video>
    </div>
      </div>
      <div className="flex flex-col items-center justify-center h-screen text-white" style={{zIndex:'999'}}>
        <Logo />
        <h2 className="text-3xl font-bold mt-2">AuRA</h2>
        <p className="mt-2">Automated React Architecture</p>
        <ButtonRow />
      </div>
      <Info />
      <GridSection title="Supported frameworks" gridLayout="2x6" />
    </div>
  );
};
export default Main;
