<?php
    require_once 'vendor/autoload.php';

    use Dompdf\Dompdf;
    use Dompdf\Options;

    $name = $_POST['name'];
    $email = $_POST['email'];
    $small_action_figures = $_POST['small_action_figures'];
    $medium_action_figures = $_POST['medium_action_figures'];
    $large_action_figures = $_POST['large_action_figures'];
    $date = date('l jS \of F Y h:i:s A');

    $small_action_figures_price = 7;
    $medium_action_figures_price = 20;
    $large_action_figures_price = 50;

    $total_small = $small_action_figures * $small_action_figures_price;
    $total_medium = $medium_action_figures * $medium_action_figures_price;
    $total_large = $large_action_figures * $large_action_figures_price;
    $total = $total_small + $total_medium + $total_large;
    

    $html = "<!DOCTYPE html>
    <html>
        <head>
            <title> Order Summary</title>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 5px;
                }
            </style>
        </head>
        <body>
            <h1 style='text-align: center;'>Action Figure Shop</h1>
            <h2> Quotation for:</h2>
            $name<br>
            $email<br>
            $date
            <h2>Order Summary</h2>
            <table>
                <thead>
                    <tr>
                        <th>Figure Type</th>
                        <th>Quantity</th>
                        <th>Price</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Small Action Figures</td>
                        <td>$small_action_figures</td>
                        <td>$small_action_figures_price\$</td>
                        <td>$total_small\$</td>
                    </tr>
                    <tr>
                        <td>Medium Action Figures</td>
                        <td>$medium_action_figures</td>
                        <td>$medium_action_figures_price\$</td>
                        <td>$total_medium\$</td>
                    </tr>
                    <tr>
                        <td>Large Action Figures</td>
                        <td>$large_action_figures</td>
                        <td>$large_action_figures_price\$</td>
                        <td>$total_large\$</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td>Total</td>
                        <td>$total\$</td>
                    </tr>
                </tbody>
            </table>
            <p> Shipping not included. </p>
            <p> If you have any questions, please contact us at sales@company.com </p>
        </body>";

    $dompdf = new Dompdf();
    $dompdf->loadHtml($html);
    $dompdf->setPaper('A4', 'landscape');

    global $_dompdf_show_warnings;
    $_dompdf_show_warnings = true;

    $dompdf->render();
    $dompdf->stream("order_summary.pdf", array(
        "Attachment" => false
    ));
?>
