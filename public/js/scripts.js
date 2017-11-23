$(document).on('click', '.nav-item', function(event) {
    $('.nav-item').each(function(event){
      $(this).classList.remove('active');
    });
    $(this).classList.add('active');
});​
