// components/Form.tsx
import React, { useState } from 'react';
const Form: React.FC = () => {
  const [selectedOption, setSelectedOption] = useState("");
  const handleOptionChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedOption(e.target.value);
  };
  return (
    <form className="form">
      <h2>Form Title</h2>
      <div className="field">
        <label className="label">Multiple Choice</label>
        <div className="control">
          <div className="select">
            <select name="multipleChoice" value={selectedOption} onChange={handleOptionChange}>
              <option>Select an option</option>
              <option>Option 1</option>
              <option>Option 2</option>
              <option>Option 3</option>
            </select>
          </div>
        </div>
      </div>
      <div className="field">
        <label className="label">Short Answer</label>
        <div className="control">
          <input className="input" type="text" placeholder="Enter your answer" />
        </div>
      </div>
      <div className="field">
        <label className="label">Textarea</label>
        <div className="control">
          <textarea className="textarea" placeholder="Enter your answer"></textarea>
        </div>
      </div>
      <div className="field is-grouped">
        <div className="control">
          <button className="button is-primary">Submit</button>
        </div>
        <div className="control">
          <button className="button is-link">Cancel</button>
        </div>
      </div>
    </form>
  );
};
export default Form;