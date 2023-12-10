# LAuRA: Loop Automated React Architecture

LAuRA (Loop Automated React Architecture) is an innovative tool designed to automate the process of web application development. Originally derived from [ChatDev](https://github.com/OpenBMB/ChatDev), it simplifies building complex web apps by leveraging AI-driven technologies.

By running a single command, users interactively enable LAuRA to generate customized web applications based on specified requirements. It supports various frameworks, libraries, and development modes, streamlining the web development workflow significantly.

This open-source project, managed by [Spark Engine AI](https://sparkengine.ai), is an ideal solution for developers seeking to rapidly prototype and develop web applications with minimal manual coding.

Join our Discord [here](https://discord.gg/fBuFBPvN6W) to join us!

## ⚡️ Quickstart

### Get Started with LAuRA in just 5 Steps!

1. **Clone the GitHub Repository:**
   ```
   git clone https://github.com/spark-engine-ai/LAuRA.git
   ```

2. **Install and Set Up LAuRA:**
   Navigate to the `LAuRA` directory where the setup.py file is and run:
   ```
   pip install -e .
   ```

3. **Set your OpenAI API Key:** Open a terminal anywhere you would like, but first remember to initialize your OpenAI API key like so:

   On Unix/Linux:

   ```
   export OPENAI_API_KEY="your_OpenAI_API_key"
   ```

   On Windows:

   ```
   $env:OPENAI_API_KEY="your_OpenAI_API_key"
   ```

   Every time you open a new terminal to use LAuRA, you must initialize the API key. (we are working to make this easier btw)

4. **Run LAuRA:**
   Now type `laura` in the command line inside any directory to begin making a project. LAuRA will guide you through a form to fill in the arguments. For a list of available arguments, you can use `laura -h`.

   Note: All project outputs will be stored in the `/laura` folder in the user's home directory.

5. **Run Your Application:**
   Note: All project outputs will appear in the `laura/projects` folder in the user's home directory.

   Navigate to it and run your application with:
   ```
   npm install
   npm run start
   ```
   Keep in mind running the project is recommended when using Human mode at the same time. This way you can see any changes that the AI makes live. Running the web app might also be npm run start, serve etc. depending on the selected stack template.

## 🎉 News

* **December 6th, 2023: Global access.** LAuRA is now accessible from any path and will soon be able to output to any path as well as iterate inside any path. Join our Discord to contribute!

* **December 3rd, 2023: Custom stack templates.** Use --stack "REACT" to use VUE, NEXT or REACT framework when building your app. We highly recommend using --config "Human" with it so you can get the AI team to iterate on the project while you host the web app locally through a second terminal window.

* **November 29th, 2023: LAuRA project initiation.** We begun building up an automated React architecture to build entire web apps locally using AI agents.

## 📝 Build your own stack templates!

* **How do I support my preferred stack?**
  - Go to the frameworks folder
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
