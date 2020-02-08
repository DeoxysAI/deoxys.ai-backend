const express = require("express");
const { PythonShell } = require("python-shell");
const cors = require("cors");
const path = require("path");
const fs = require("fs");
const multer = require("multer");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use("/stargan/resultImg", express.static("stargan/resultImg"));

app.use(cors());

let upload = multer({ dest: path.join(__dirname, "stargan/upload/") });

app.get("/text/", (req, res) => {
	PythonShell.run("filename-text.py", null, (err, result) => {
		if (err) throw err;
		res.send(result);
	});
});

app.get("/random-image", (req, res) => {
	PythonShell.run("filename-image.py", null, (err, result) => {
		if (err) throw err;
		res.send(filename); // send filename
	});
});

app.post("/image", upload.single("file"), (req, res) => {
	const tempPath = req.file.path;
	const targetPath = path.join(
		__dirname,
		`./stargan/images/${req.file.originalname}`
	);
	fs.rename(tempPath, targetPath, err => {
		if (err) throw err;
		else {
			console.log("RENAMING DONE");
			PythonShell.run(
				"./stargan/preprocessingImg.py",
				{ args: [req.file.originalname, req.params.flag] },
				(err, result1) => {
					if (err) throw err;
					console.log("PREPROCESSING DONE");
					PythonShell.run(
						`stargan/main.py`,
						{
							args: [
								"CelebA",
								"Black_Hair Blond_Hair Young Male Oval_Face"
							]
						},
						(err, result2) => {
							if (err) throw err;
							console.log(result2);
							console.log("MODEL DONE");
							res.send(result2);
						}
					);
				}
			);
		}
	});
});

const PORT = process.env.PORT || 9828;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
