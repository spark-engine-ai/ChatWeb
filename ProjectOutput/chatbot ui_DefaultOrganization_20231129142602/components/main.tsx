import React, { useState } from 'react';
import ChatInput from './ChatInput';
import ChatMessages from './ChatMessages';
const Main: React.FC = () => {
  const [chatMessages, setChatMessages] = useState<string[]>([]);
  const handleSendMessage = (message: string) => {
    if (message.trim() !== '') {
      setChatMessages((prevMessages) => [...prevMessages, message]);
    }
  };
  return (
    <div className="flex flex-col h-screen">
      <div className="flex-grow">
        <ChatMessages chatMessages={chatMessages} />
      </div>
      <div className="border-t border-gray-200">
        <ChatInput handleSendMessage={handleSendMessage} />
      </div>
    </div>
  );
};
export default Main;