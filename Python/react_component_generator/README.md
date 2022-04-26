# React Component Generator

This python script creates javascript files with basic boilerplate for a react functional component in their respective folders.

You need a json file with 2 properties

**folder**  
this is the folder that will contain the components

**components**  
an array of components to be created in the folder. Each component will be created within a sub-folder with the same name

## Example

**config.json**

```js
{
  "folder": "pages",
  "components": ["login", "register", "home"]
}
```

The above configuration implies that you want to create a folder called **pages** with 3 sub-folders **( login, register, home )** each containing a react component with the same name **( Login.js, Register.js, Home.js )**

The eventual folder struture would look like this

> - pages/
>   - login/
>     - Login.js
>   - register/
>     - Register.js
>   - home/
>     - Home.js

and each javascript file will contain

```js
// libraries
import React from "react";

// other components

// style

// utils

const ComponentName = () => {
  return <div>This is the {component name} component</div>;
};

export default ComponentName;
```

## Running the script

You must pass the config file as an argument like so

```py
python create.py config.json
```

## Miscillaneous

seen a bug?
wanna improve it?

create an issue or pull request 🚀
