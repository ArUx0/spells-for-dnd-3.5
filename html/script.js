console.log(spells_long);

function ini_spells_short(data){

    html = '';
    prev_class = '';
    prev_lvl = '';

    $.each(data, function(key, value){

        CLASS = value.CLASS;
        SPELL_LEVEL = value.SPELL_LEVEL;
        SPELL_NAME = value.SPELL_NAME;
        SPELL_SHORT_DESCRIPTION = value.SPELL_SHORT_DESCRIPTION;

        if(prev_class != CLASS){

            if( key != 0 ){
                html += '</div>'; //class_content end
            html += '</div>'; //class_container end
            }

            html += '<div class = "class_container spells_short '+value.CLASS+'">';
                html += '<div class = "class_label spells_short '+value.CLASS+'">';
                    html += value.CLASS;  
                html += '</div>';
                html += '<div class = "class_content spells_short '+value.CLASS+'">';
        }
            if(prev_lvl != SPELL_LEVEL){

                if( key != 0 ){
                html += '</div>'; //level_container end
                }

                html += '<div class = "level_container spells_short '+value.CLASS+' '+value.SPELL_LEVEL+'">';
                    html += '<div class = "level_label spells_short '+value.CLASS+' '+value.SPELL_LEVEL+'">';
                        html += 'Poziom czaru:  <b>' + value.SPELL_LEVEL + '</b>';  
                    html += '</div>';
                    html += '<div class = "level_content spells_short '+value.CLASS+' '+value.SPELL_LEVEL+'">';
            }
                        html += '<div class = "spell_container spells_short '+value.CLASS+' '+value.SPELL_LEVEL+'">';
                            html += '<div class = "spell_label spells_short '+value.CLASS+' '+value.SPELL_LEVEL+'">';
                                html += value.SPELL_NAME;  
                            html += '</div>';  
                            html += '<div class = "spell_content spells_short '+value.CLASS+' '+value.SPELL_LEVEL+'">';
                                html += value.SPELL_SHORT_DESCRIPTION; 
                                html += '<div class = "spell_long_description spells_short '+value.CLASS+' '+value.SPELL_LEVEL+'">';
                                    html += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";  
                                html += '</div>';  
                            html += '</div>';  
                        html += '</div>';

            
                if(prev_lvl == SPELL_LEVEL && key == data.length - 1 && key != 0){
                html += '</div>'; //level_container end
                }

            if(prev_class == CLASS && key == data.length - 1 && key != 0){
                html += '</div>'; //class_content end
            html += '</div>'; //class_container end
            }
           
            
            prev_class = CLASS;
            prev_lvl = SPELL_LEVEL;
            
        });

    $(".main_container.spells_short .main_content").append(html);

}


$(document).on("click", ".spell_container",function(){
    $(this).find(".spell_long_description").toggleClass("active");
    $(this).toggleClass("active");
});