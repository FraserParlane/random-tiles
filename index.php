<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tiles</title>
    <link rel="stylesheet" href="main.css" />
</head>
<body>
    <div class="tile-container">
        <!-- Tile overlays -->
        <div class="tile-overlay" style="--x: 8; --y: 1; --x-pos: 1; --y-pos: 1;">
            Fraser Parlane, PhD
        </div>
        <div class="tile-overlay" style="--x: 3; --y: 1; --x-pos: 1; --y-pos: 2;"></div>

        <?php
            $files = scandir('tiles');
            foreach(array_values($files) as $i => $file) {
                if($file !== "." && $file !=="..") {
                    echo "<img src='tiles/$file' class='tile' id='tile_$i'/>";
                }
            }
        ?>

    </div>


    <div class="dummy-text">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id nulla turpis. Aliquam et convallis ipsum, et vestibulum ante. Cras elementum gravida sem ut ornare. Ut nec magna erat. Praesent sit amet neque at erat sodales viverra ut nec est. Mauris rutrum metus eu imperdiet placerat. Vivamus egestas non lacus nec consequat. Duis placerat quam nec consequat vestibulum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed accumsan elit a nisl dapibus venenatis at vitae leo. Aenean egestas facilisis molestie. Aliquam tincidunt volutpat elit nec suscipit. Pellentesque accumsan augue in egestas accumsan.

        Nunc rhoncus ac sapien eu ultricies. Curabitur nibh nibh, fermentum eu velit tempor, gravida egestas massa. Vivamus non auctor neque. Nulla cursus diam risus, sit amet posuere metus eleifend a. Integer a placerat tellus. Donec nibh neque, vestibulum nec nulla sed, volutpat accumsan ex. Maecenas at consequat tortor. Nunc vel lectus ante. Duis felis justo, euismod ut feugiat vitae, sagittis quis felis. Nam at diam vitae nibh accumsan volutpat ac vel lectus. In pellentesque aliquam scelerisque. Nullam molestie metus arcu, vitae efficitur mi viverra vitae. Suspendisse dignissim, eros quis rutrum pretium, tellus felis iaculis ipsum, vel blandit magna velit id arcu. Pellentesque laoreet orci vitae orci rhoncus, quis lobortis tellus euismod. Proin euismod turpis at laoreet fringilla. Etiam iaculis nisi eu fringilla semper.

        Cras quis commodo massa. In eget est magna. Nunc ut tortor non leo tincidunt consectetur. Maecenas malesuada tincidunt purus. Aenean ut convallis dui. Etiam dictum vehicula velit, et aliquam dolor sollicitudin non. Mauris vel aliquet nunc. Nam sodales dolor non dignissim auctor. Sed nibh odio, fermentum elementum vehicula sit amet, rutrum sed ante. Vestibulum lacus mauris, venenatis non sollicitudin vel, malesuada in metus. Nullam ornare a est et laoreet.

        Fusce sollicitudin dolor quis velit rhoncus laoreet. Cras vitae varius turpis, sit amet laoreet ante. Pellentesque quis fringilla purus. Sed condimentum dolor at quam aliquam, eu facilisis enim faucibus. Sed blandit sit amet justo at aliquet. Sed fringilla, mauris sed rutrum tristique, purus ligula bibendum nisi, fermentum rutrum eros tortor eget velit. Nunc convallis a est eget tristique.

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis aliquam neque vel volutpat. Sed tristique, ipsum ut posuere congue, quam dui bibendum urna, quis interdum justo eros sit amet purus. Curabitur non ornare dolor, feugiat congue ante. Curabitur eu pretium purus, eget vulputate turpis. Morbi sed risus ut augue finibus tincidunt. Donec sem arcu, posuere quis sodales nec, maximus at nisl. Integer vel congue eros. Etiam imperdiet turpis neque, at finibus libero maximus ac. Suspendisse ut eleifend massa, eu euismod metus.
    </div>
</body>
</html>