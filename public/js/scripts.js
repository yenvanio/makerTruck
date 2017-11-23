$(document).on('click', '.nav-link', function(event) {
    $('.nav-item').each(function(event){
      $(this).classList.remove('active');
    });
    $(this).parent().classList.add('active');
});​
