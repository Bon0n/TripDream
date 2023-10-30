$("#formAdd select[name='state']").on('change', function(){
        $(".after").text("");
        var $this = $(this);
        if($this.val() != ''){
            $.ajax({
                url: '/'+$this.val(),
                type: 'GET',
                success: function(resp){
                    let options = '';
                    resp.data.forEach(city => {
                        options+='<option value='+city.id+'>'+city.city+'</option>';
                    });
                    $("#formAdd select[name='city']").find('.after').after(options);
                },
                error: function(resp){
                    console.log('Something went wrong');
                }
            });
        }else {
            $("#formAdd select[name='city']").find('.after').nextAll().remove();
        }
});