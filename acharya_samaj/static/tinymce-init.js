var script = document.createElement('script');
script.type = 'text/javascript';
script.src = 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js';
document.head.appendChild(script);

script.onload = function () {
    tinymce.init({
        selector: '#id_description',
        plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreaker spellchecker',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            'table emoticons template paste help'
        ],
        toolbar: 'undo redo | formatselect | bold italic | alignleft aligncenter alignright | bullist numlist outdent indent | link image | code',
        // menubar: false,
        // branding: false,
        statusbar: true,
        // language: '{{ language }}',
        // height: 300,
        setup: function (editor) {
            editor.on('change', function () {
                editor.save();
            });
        }
    });
}