if (typeof jqXhr.success != 'undefined') {
    $('#success-modal').modal('show');
} else {
    $('#contact').html(jqXhr);
}