document.addEventListener('DOMContentLoaded', function () {
    const modalElement = document.getElementById('addProductModal');
    if (!modalElement) {
        return;
    }

    modalElement.addEventListener('hidden.bs.modal', function () {
        const form = modalElement.querySelector('form');
        if (form) {
            form.reset();
        }
    });
});
