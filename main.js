$(document).ready(function () {
    $.getJSON("./data.json", function(data) {
        var stocks_data = '';
        $.each(data, function (key, value) { 
             stocks_data += '<tr class="rounded">';
             stocks_data += '<td>' + value.name + '</td>';
             stocks_data += '<td>' + value.perc + '</td>';
             stocks_data += '<td>' + value.price + ' SEK</td>';
             stocks_data += '</tr>';
        });
        $('.table').append(stocks_data);
    });
});