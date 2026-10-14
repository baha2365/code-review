// weak code
const express = require("express");
const path = require("path");
const fs = require("fs");
const app = express();

const BASE = path.join(__dirname, "reports");

app.get("/reports/download", (req, res) => {
    const name = req.query.name;
    if (name.includes("../")) {
        return res.status(400).send("Invalid name");
        }
    const target = path.join(BASE, decodeURIComponent(name));
    if (!fs.existsSync(target)) {
        return res.status(404).send("Not found");
    }
    res.download(target);
});

app.listen(3000);


// 