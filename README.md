# ChatWeb: Web Application Development Made Easy

Originally forked from [ChatDev](https://github.com/OpenBMB/ChatDev).

Open source, updated and maintained by our contributors. Managed by the team at [Spark Engine AI](https://sparkengine.ai).

Join our Discord [here](https://discord.gg/fBuFBPvN6W) to join us!

## ⚡️ Quickstart

### Getting Started with ChatWeb

Follow these steps to set up and run ChatWeb:

1. **Clone the GitHub Repository:**
   ```
   git clone https://github.com/spark-engine-ai/ChatWeb.git
   ```

2. **Set Up the Python Environment:**
   Ensure you have Python 3.9 or higher. Create and activate an environment:
   ```
   conda create -n ChatWeb_env python=3.9 -y
   conda activate ChatWeb_env
   ```

3. **Install Dependencies:**
   Navigate to the `ChatWeb` directory and install required packages:
   ```
   cd ChatWeb
   pip3 install -r requirements.txt
   ```

4. **Set OpenAI API Key:** Export your OpenAI API key as an environment variable. Replace `"your_OpenAI_API_key"` with
  your actual API key. Remember that this environment variable is session-specific, so you need to set it again if you
  open a new terminal session.
  On Unix/Linux:

  ```
  export OPENAI_API_KEY="your_OpenAI_API_key"
  ```

  On Windows:

  ```
  $env:OPENAI_API_KEY="your_OpenAI_API_key"
  ```

5. **Build Your Application:** Use the following command to initiate the building of your application,
  replacing `[description_of_your_idea]` with your idea's description and `[project_name]` with your desired project
  name:
  On Unix/Linux:

  ```
  python3 run.py --task "[description_of_your_idea]" --name "[project_name]"
  ```

  On Windows:

  ```
  python run.py --task "[description_of_your_idea]" --name "[project_name]"
  ```

6. **Run Your Application:**
   Access your project in the `ProjectOutput` directory. Run your application with:
   ```
   cd ProjectOutput/<project_name>_timestamp
   npm install
   npm run dev
   ```

## 🎉 News

* **November 29th, 2023: ChatWeb project initiation.** Currently supporting Next JS, TypeScript, and Tailwind for efficient web app development.

## 🛠️ Currently Supported Technologies

- **Frameworks and Libraries:** Next JS, TypeScript, Tailwind CSS.
- **Modes:** Only the default mode is currently supported.

## 📝 To-Do List

- **Adding UI Kits:**
  - Mantine UI
  - Chakra UI
  - Ant UI
  - Materialize UI
  - Bootstrap UI
  - etc.

- **Adding Frameworks:**
  - React Native
  - Express
  - Vue
  - CRA (Create React App)
  - Grommet
  - Gatsby
  - React Bootstrap
  - Angular
  - Node.js
  - Remix
  - Redux
  - etc.

- **Adding Icon Libraries:**
  - Tabler Icons
  - React Icons
  - Ant UI Icons
  - etc.

- **Future Features:**
  - Mix and match JS/TS, UI kits, and frameworks based on arguments.
  - A component library for AI to select from prop-based components.
  - More modular configurations and custom config options.
  - Ability to navigate and create subfolders.
  - API building support.
  - Detect and iterate on project frameworks of existing projects.
  - SVG and PNG library plugins via Pexels and other royalty free image APIs
  - DALLE 3 image creation

## 📬 Contact

For questions, feedback, or collaborations, reach out to us at our [Spark Engine](mailto:jordan@sparkengine.ai) email.
