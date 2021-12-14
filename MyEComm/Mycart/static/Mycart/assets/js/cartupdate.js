
if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}
var sum = 0;
for (item in cart) {

    let name = cart[item][1];
    let qty = cart[item][0];
    sum = sum + qty;
    mystr = `        <li class="list-group-item d-flex justify-content-between align-items-center">
               ${name}
                <span class="badge badge-primary badge-pill">${qty}</span>
            </li>`
    $('#items').append(mystr);
}
document.getElementById('cart').innerHTML = sum;
$('#order_json').val(JSON.stringify(cart));


$(document).ready(function(){
    $("#checkoutpage").click(function(){
      $(this).attr("href", "/Mycart/checkout");
    });
  });
  
