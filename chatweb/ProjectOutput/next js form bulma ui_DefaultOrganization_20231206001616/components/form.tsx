import React from 'react';
import MultipleChoice from './MultipleChoice';
import ShortAnswer from './ShortAnswer';
import Textarea from './Textarea';
const Form: React.FC = () => {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new FormData(e.target as HTMLFormElement);
    const multipleChoiceValue = formData.get('multiple-choice');
    const shortAnswerValue = formData.get('short-answer');
    const textareaValue = formData.get('textarea');
    console.log('Multiple Choice:', multipleChoiceValue);
    console.log('Short Answer:', shortAnswerValue);
    console.log('Textarea:', textareaValue);
    // Handle form submission logic here
  };
  return (
    <form onSubmit={handleSubmit}>
      <h2 className="text-2xl font-bold mb-4">Form Title</h2>
      <MultipleChoice />
      <ShortAnswer />
      <Textarea />
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 mt-4">
        Submit
      </button>
    </form>
  );
};
export default Form;