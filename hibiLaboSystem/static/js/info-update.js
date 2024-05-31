$(document).ready(function () {

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#image-preview').attr('src', e.target.result);
                $('#image-preview-1').attr('src', e.target.result).css('display', 'block')
                $('#delete-image').css('display', 'block')

            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    $('#id_image').change(function () {
        readURL(this);
    });

    $('#delete-image').click(function () {
        
        $('#image-preview').attr('src', image)
        $(this).css('display', 'none')
        $("#id_image").val("")

        if(!image){
            $('#image-preview-1').attr('src', image).css('display', 'none')
        }
    })

})