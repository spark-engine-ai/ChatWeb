import React, { useState } from 'react';
interface ChatInputProps {
  handleSendMessage: (message: string) => void;
}
const ChatInput: React.FC<ChatInputProps> = ({ handleSendMessage }) => {
  const [message, setMessage] = useState('');
  const handleMessageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setMessage(e.target.value);
  };
  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSendMessage(message);
      setMessage('');
    }
  };
  const handleSendMessageClick = () => {
    handleSendMessage(message);
    setMessage('');
  };
  return (
    <div className="p-4 flex items-center">
      <input
        type="text"
        value={message}
        onChange={handleMessageChange}
        onKeyPress={handleKeyPress}
        placeholder="Type your message..."
        className="flex-grow border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        onClick={handleSendMessageClick}
        className="ml-4 bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md"
      >
        Send
      </button>
    </div>
  );
};
export default ChatInput;