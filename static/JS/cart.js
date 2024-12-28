document.addEventListener('DOMContentLoaded', () => {
    let total = 0;
    const totalAmountElement = document.getElementById('total__amount');
    const checkoutButton = document.querySelector('.checkout__button');

    // tổng tiền
    document.querySelectorAll('.cart__total').forEach(cell => {
        total += parseInt(cell.textContent.trim());
    });
    totalAmountElement.textContent = total.toLocaleString('vi-VN');

    if (total > 0) {
        checkoutButton.disabled = false;
    }
    checkoutButton.addEventListener('click', () => {
        const cartItems = Array.from(document.querySelectorAll('.cart__row')).map(row => {
            const productId = row.querySelector('input[name="product_id"]').value;
            const quantity = parseInt(row.querySelector('.cart__number').textContent.trim());
            return {
                product_id: productId,
                quantity: quantity
            };
        });
        fetch('/process_order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ cart_items: cartItems })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Đặt thành công, mã đơn: ' + data.order_id);
                window.location.href = '/';
            } else {
                alert('Đặt thất bại: ' + data.message);
            }
        })
    });
});
