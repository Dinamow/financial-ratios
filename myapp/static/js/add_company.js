document.addEventListener('DOMContentLoaded', function() {
    const addedAlert = document.querySelector('.added-alert');

    if (addedAlert) {
        setTimeout(() => {
            addedAlert.classList.add('hidden');

            addedAlert.addEventListener('transitionend', function() {
                addedAlert.remove();
            }, { once: true });
        }, 5000);
    }
});
