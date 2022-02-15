var clicked;
$(".send-order").click(function () {
    let ordersValue = cart
    var json = JSON.stringify(ordersValue);
    $.ajaxSetup({
        headers: {"X-CSRFToken": '{{csrf_token}}'}
    });
    $.ajax({
        type: "POST",
        url: "{% url 'test1' %}",
        data: json,
        dataType: "json",
        success: function (msg) {
            console.log(msg)
        },
        error: function (msg) {
            alert("Error !");
        }
    });
});