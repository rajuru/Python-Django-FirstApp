jQuery(document).ready(function(){
    $(document).on('dblclick', 'h1.topic_name', function(e){
        $('input.topic_name').show();
        $(this).hide();
    })
    $(document).on('blur','input.topic_name', function(e){
        data = {
            topic_guid: $('#topic_form').attr('data-topic-guid'),
            topic_title: $(this).val()
        };
        $('h1.topic_name').html(data.topic_title).show();
        $(this).hide();
        $.post('/topics/'+ data.topic_guid + '/update/',
                data
            ,
            function(data){
                console.log(data)
            }
        )

    })
})