document.addEventListener('DOMContentLoaded', function () {
    // Получаем сообщения Django из контекста
    const messages = JSON.parse(document.getElementById('django-messages').textContent);

    // Проверяем, есть ли сообщения
    if (messages.length > 0) {
        const toastElement = document.getElementById('notificationToast');
        const toastBody = toastElement.querySelector('.toast-body');

        // Обрабатываем каждое сообщение
        messages.forEach(message => {
            // Устанавливаем текст уведомления
            toastBody.textContent = message.message;

            // Устанавливаем цвет фона в зависимости от уровня сообщения
            if (message.level === 'success') {
                toastElement.classList.remove('text-bg-danger');
                toastElement.classList.add('text-bg-success');
            } else if (message.level === 'error') {
                toastElement.classList.remove('text-bg-success');
                toastElement.classList.add('text-bg-danger');
            }

            // Инициализация и показ Toast
            const toast = new bootstrap.Toast(toastElement, {
                autohide: true,
                delay: 3000, // Время отображения (в миллисекундах)
            });
            toast.show();
        });
    }
});