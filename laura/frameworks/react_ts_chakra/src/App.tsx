import React from 'react';
import logo from './logo.svg';
import './App.css';
import Main from './components/main';
import { ChakraBaseProvider } from '@chakra-ui/react';

function App() {
  return (
    <div className="App">
      <ChakraBaseProvider>
     <Main />
     </ChakraBaseProvider>
    </div>
  );
}

export default App;
