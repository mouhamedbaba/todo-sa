const express = require("express");
const path = require("path");
const cookieParser = require("cookie-parser");
const { log } = require("console");

const app = express();

const homePage = path.resolve(__dirname, "./index.html");
app.use(express.static("./public"));
app.use(cookieParser());


function AuthMw (req, res, next) {
  const user = req.cookies.user; // Verify user in cookies
  log("md is runnind")
  if (user) {
    return res.redirect("/login");
  }
  next()  
}

app.get("/", AuthMw, (req, res, next) => {
  res.status(200).sendFile(homePage);
});

// Login route for demonstration
app.get("/login", (req, res) => {
  res.send("<h1>Please login</h1>");
});

app.all("*", (req, res) => {
  res.status(404).send("<h1>Resource NOT FOUND</h1>");
});

app.listen(3000, () => {
  console.log("app is listening on port 3000");
});
