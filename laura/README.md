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
   Access your project in the `projects` directory. Run your application with:
   ```
   cd projects/<project_name>_timestamp
   npm install
   npm run start
   ```
   Keep in mind running the project is recommended when using Human mode at the same time. This way you can see any changes that the AI makes live. Running the web app might also be npm run start, serve etc. depending on the selected stack template.

## 🎉 News

* **December 3rd, 2023: Custom stack templates!.** Use --stack "REACT" to use VUE, NEXT or REACT framework when building your app. We highly recommend using --config "Human" with it so you can get the AI team to iterate on the project while you host the web app locally through a second terminal window.

* **November 29th, 2023: ChatWeb project initiation.** We begun building up an automated React architecture to build entire web apps locally using AI agents.

## 📝 Build your own stack templates!

* **How do I support my preferred stack?**
  - Go to the ProjectConfig folder
  - Create a json like the templates we already have
  - Specify the framework and UI kit
  - Set up a starter template folder for it like the ones we have and make sure to import a components/main file into the index of the project. The AI will automatically generate this main.tsx file when you initialize and locally clone the stack template.
  - Go back to the json and specify the path to your templates components folder so it knows where to make the main.tsx

## 🛠️ Currently Supported Technologies

- **Frameworks and Libraries:** React.js, Next.js, Vue.js, TypeScript, Tailwind CSS, React Icons.
- **Modes:** Only the default and human mode is currently supported.

## 📝 To-Do List

- **Adding Frameworks:**
  - React.js ✓
  - Next.js ✓
  - Vue.js ✓
  - Angular.js
  - etc.

- **Adding UI Kits:**
  - Tailwind ✓
  - Mantine
  - Chakra
  - Ant
  - Materialize
  - Bootstrap
  - etc.

- **Adding Icon Libraries:**
  - React Icons ✓
  - Tabler Icons
  - Ant UI Icons
  - etc.

- **Future Features:**
  - Mix and match JS/TS, UI kits, and frameworks. ✓
  - A component library for AI to select from prop-based components.
  - More modular configurations and custom config options. ✓
  - Ability to navigate and create subfolders.
  - API building support.
  - Detect and iterate existing projects.
  - SVG and PNG library plugins via Pexels and other royalty free image APIs
  - DALLE 3 image creation

## 📬 Contact

For questions, feedback, or collaborations, reach out to us at our [Spark Engine](mailto:jordan@sparkengine.ai) email.
