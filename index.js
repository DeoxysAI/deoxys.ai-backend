const express = require("express");
const { PythonShell } = require("python-shell");
const path = require("path");
const fs = require("fs");
const multer = require("multer");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

let upload = multer({ dest: path.join(__dirname, "upload/") });

app.get("/text/:flag", (req, res) => {
	PythonShell.run("filename-text.py", null, (err, result) => {
		if (err) throw err;
		res.send(result);
	});
});

app.get("/random-image", (req, res) => {
	// the below line will go in the callback of the pythonshell
	PythonShell.run("filename-image.py", null, (err, result) => {
		if (err) throw err;
		res.sendFile(path.join(__dirname, `./stargan/resultImg/${result2}`));
	});
});

app.post("/image/:flag", (req, res) => {
	const tempPath = req.file.path;
	const targetPath = path.join(
		__dirname,
		`./uploads/${req.file.originalname}`
	);
	fs.rename(tempPath, targetPath, err => {
		if (err) throw err;
		else {
			PythonShell.run(
				"./stargan/preprocessingImg.py",
				[req.file.originalname, req.params.flag],
				(err, result1) => {
					if (err) throw err;
					PythonShell.run(
						`./stargan/main.py --mode test --dataset CelebA --image_size 128 --selected_attrs ${req.params.flag} --c_dim 1 --celeba_image_dir ../images --attr_path newAttr.txt --model_save_dir stargan_celeba_128/models --result_dir resultImg`,
						null,
						(err, result2) => {
							res.sendFile(
								path.join(
									__dirname,
									`./stargan/resultImg/${result2}`
								)
							);
						}
					);
				}
			);
		}
	});
});

const PORT = process.env.PORT || 9828;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
