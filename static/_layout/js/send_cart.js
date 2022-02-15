var clicked;
$(".send-order").click(function () {
    let ordersValue = cart
    var json = JSON.stringify(ordersValue);
    $.ajaxSetup({
        headers: {"X-CSRFToken": '{{csrf_token}}'}
    });
    $.ajax({
        type: "POST",
        url: "{% url '/customers/test/' %}",
        data: json,
        dataType: "json",
        success: function (msg) {
            console.log(msg)
        },
        error: function (msg) {
            alert("jbkvbwrb");
        }
    });
});