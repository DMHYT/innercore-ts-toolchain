#### **[-> Russian <-](README.ru.md)**
# **innercore-ts-toolchain**
### **Simple toolchain for writing InnerCore mods on TypeScript / JavaScript.**
***
## **Requirements**
* **[Python](https://www.python.org/) 3.6 or higher**
* **[node.js](https://nodejs.org/en/) 10.15.1 or higher**
* **TypeScript node package installed globally using `npm install --g typescript`**
* **[Visual Studio Code](https://code.visualstudio.com/) and [TypeScript Auto Compiler](https://marketplace.visualstudio.com/items?itemName=morissonmaciel.typescript-auto-compiler) extension for it**
***
## **Project setup**
### To setup new mod project, firstly create a new folder, then create `setup.py` file in it, and copy and paste the code from [here](setup.py). Execute the file, put some params in the input line and here it is, your project is set up successfully. Open your project's folder with VSCode and enjoy mod development on TypeScript.
***
## **VSCode build tasks**
### The toolchain provides you with two build tasks for VSCode, the first is `Download docs`, which downloads newest InnerCore TypeScript declarations from [docs website](https://docs.mineprogramming.org), and the second is `Build mod`, which builds all your code, which you previously specified in `tsconfig.json` in `include` parameter in needed order, into `main.js` file in output mod folder. The tab for choosing one of the tasks is called by pressing `Ctrl + Shift + B`.
***
## **Other information**
### [My VK](https://vk.com/vstannumdum)
### [My VK Public for InnerCore mods](https://vk.com/dmhmods)
### [My YouTube channel](https://youtube.com/c/DMH_Minecraft)