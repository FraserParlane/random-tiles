<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tiles</title>
    <link rel="stylesheet" href="main.css" />
</head>
<body>
    <?php
        $files = scandir('tiles');
        foreach($files as $file) {
            if($file !== "." && $file !=="..") {
                echo "<img src='tiles/$file' />";
            }
        }
    ?>
</body>
</html>