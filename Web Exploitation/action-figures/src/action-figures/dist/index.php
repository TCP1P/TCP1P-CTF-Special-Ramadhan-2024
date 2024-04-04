<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Action Figure Shop</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>

    <header class="bg-primary text-white text-center py-2">
        <h1>Action Figure Shop</h1>
    </header>
    <main class="container my-4">
        <p class="text-left">High quality action figures at affordable prices. Our automated service will calculate the price for your action figures. Once you are done, get in contact with us to complete your order.</p>
        <form action="order.php" method="post">
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" name="name" placeholder="Enter your name" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" name="email" placeholder="Enter your email" required>
            </div>
            <div class="mb-3">
                <label for="small_action_figures" class="form-label">Small Action Figures</label>
                <input type="number" class="form-control" id="small_action_figures" name="small_action_figures" placeholder="Enter number of small action figures" required>
            </div>
            <div class="mb-3">
                <label for="medium_action_figures" class="form-label">Medium Action Figures</label>
                <input type="number" class="form-control" id="medium_action_figures" name="medium_action_figures" placeholder="Enter number of medium action figures" required>
            </div>
            <div class="mb-3">
                <label for="large_action_figures" class="form-label">Large Action Figures</label>
                <input type="number" class="form-control" id="large_action_figures" name="large_action_figures" placeholder="Enter number of large action figures" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
</body>
</html>