// components/main.tsx
import React from 'react';
import Header from './header';
import Hero from './hero';
import Features from './features';
import Footer from './footer';
const Main: React.FC = () => {
  return (
    <div>
      <Header />
      <Hero />
      <Features />
      <Footer />
    </div>
  );
};
export default Main;