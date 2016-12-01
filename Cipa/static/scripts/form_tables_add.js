if($('#nombre_formato').text() == 'Registro de Sesiones y Donativos'){
	$('#sesiones_donativos_table > tbody:last-child').append('<tr id="last_line_sesiones"><td><input name="sesiones_donativos_table_col_1_1" type="text" class="form-control"/></td> <td><input name="sesiones_donativos_table_col_1_2" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_1_3" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_1_4" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_1_5" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_1_6" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_1_7" type="text" class="form-control"/></td></tr>');
	
	function agregar_linea_sesion(){
		var numero = Number($("#filas_sesiones_donativos_table").val())+1;
		$("#last_line_sesiones").unbind();
		$("#last_line_sesiones").removeAttr( "id" );
		$('#sesiones_donativos_table > tbody:last-child').append('<tr id="last_line_sesiones"><td><input name="sesiones_donativos_table_col_'+numero+'_1" type="text" class="form-control"/></td> <td><input name="sesiones_donativos_table_col_'+numero+'_2" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_'+numero+'_3" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_'+numero+'_4" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_'+numero+'_5" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_'+numero+'_6" type="text" class="form-control"/></td><td><input name="sesiones_donativos_table_col_'+numero+'_7" type="text" class="form-control"/></td></tr>');
		$("#filas_sesiones_donativos_table").val(numero);
		$("#last_line_sesiones").on('click', agregar_linea_sesion);
	}
	$("#last_line_sesiones").on('click', agregar_linea_sesion);
}

if($('#nombre_formato').text() == 'Historia Psicológica de Clientes Menores de Edad'){
	$('#relacion_personas_viven > tbody:last-child').append('<tr id="last_line_personas_viven"><td><input name="relacion_personas_viven_col_1_1" type="text" class="form-control"/></td><td><input name="relacion_personas_viven_col_1_2" type="text" class="form-control"/></td><td><input name="relacion_personas_viven_col_1_3" type="text" class="form-control"/></td><td><input name="relacion_personas_viven_col_1_4" type="text" class="form-control"/></td></tr>');
	function agregar_linea_personas_viven(){
		var numero = Number($("#filas_relacion_personas_viven").val())+1;
		$("#last_line_personas_viven").unbind();
		$("#last_line_personas_viven").removeAttr( "id" );
		$('#relacion_personas_viven > tbody:last-child').append('<tr id="last_line_personas_viven"><td><input name="relacion_personas_viven_col_'+numero+'_1" type="text" class="form-control"/></td><td><input name="relacion_personas_viven_col_'+numero+'_2" type="text" class="form-control"/></td><td><input name="relacion_personas_viven_col_'+numero+'_3" type="text" class="form-control"/></td><td><input name="relacion_personas_viven_col_'+numero+'_4" type="text" class="form-control"/></td></tr>');
		$("#filas_relacion_personas_viven").val(numero);
		$("#last_line_personas_viven").on('click', agregar_linea_personas_viven);
	}
	$("#last_line_personas_viven").on('click', agregar_linea_personas_viven);
	
	
	
	$('#relacion_personas_familiares > tbody:last-child').append('<tr id="last_line_personas_fuera"><td><input name="relacion_personas_familiares_col_1_1" type="text" class="form-control"/></td><td><input name="relacion_personas_familiares_col_1_2" type="text" class="form-control"/></td><td><input name="relacion_personas_familiares_col_1_3" type="text" class="form-control"/></td><td><input name="relacion_personas_familiares_col_1_4" type="text" class="form-control"/></td></tr>');
	function agregar_linea_personas_fuera(){
		var numero = Number($("#filas_relacion_personas_familiares").val())+1;
		$("#last_line_personas_fuera").unbind();
		$("#last_line_personas_fuera").removeAttr( "id" );
		$('#relacion_personas_familiares > tbody:last-child').append('<tr id="last_line_personas_fuera"><td><input name="relacion_personas_familiares_col_'+numero+'_1" type="text" class="form-control"/></td><td><input name="relacion_personas_familiares_col_'+numero+'_2" type="text" class="form-control"/></td><td><input name="relacion_personas_familiares_col_'+numero+'_3" type="text" class="form-control"/></td><td><input name="relacion_personas_familiares_col_'+numero+'_4" type="text" class="form-control"/></td></tr>');
		$("#filas_relacion_personas_familiares").val(numero);
		$("#last_line_personas_fuera").on('click', agregar_linea_personas_fuera);
	}
	$("#last_line_personas_fuera").on('click', agregar_linea_personas_fuera);
	
	
	var lista_conductas_preescolares = ["Mostró respuesta a la madre", "Volteó la cabeza", "Balbuceó (expresó sonidos)", "Gateó", "Caminó sin ayuda", "Se sentó sin ayuda", "Dijo su primera palabra", "Unió varias palabras", "Logró control de esfínteres (no orinarse)", "Se mantuvo seco en la noche", "Se alimentó sin ayuda", "Manejó triciclo"]; 
	$.each( lista_conductas_preescolares, function( i, l ){
		var j = i+1;
		$('#conductas_preescolar > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="conductas_preescolar_col_'+j+'_1" type="text" class="form-control"/></td><td><input name="conductas_preescolar_col_'+j+'_2" type="text" class="form-control"/></td></tr>')
	});
	
	
	var lista_instituciones_educativas = ["Preescolar", "Primaria", "Secundaria", "Diversificado"];
	$.each( lista_instituciones_educativas, function( i, l ){
		var j = i+1;
		$('#instituciones_educativas > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="instituciones_educativas_col_'+j+'_1" type="text" class="form-control"/></td><td><input name="instituciones_educativas_col_'+j+'_2" type="text" class="form-control"/></td></tr>')
	});
	
	var lista_problemas_escolares = ["Dificultades con la lectura", "Dificultades para llevar al material de la escuela a la casa o viceversa", "Dificultades con la escritura", "Malos hábitos de estudio", "Dificultades con la matemática", "Dificultades para participar en la clase", "Dificultades con la ortografía", "Dificultades para hacer amigos", "Dificultades con la psicomotricidad fina", "Dificultades para comunicarse con sus profesores", "Dificultades con la psicomotricidad gruesa", "Dificultades para aprender otra idioma", "Dificultades con la atención", "Dificultades para hacer deporte", "Dificultades con la concentración", "No entra a clases", "Dificultades con la memoria", "Dificultades para cumplir con las normas", "Dificultades para tomar notas", "No le gusta ir al colegio", "Dificultades para estudiar", "Está molestando a otro(a)s estudiantes", "Dificultades para apuntar tareas", "Está siendo molestado(a) por otro(a)s estudiantes"];
	$.each( lista_problemas_escolares, function( i, l ){
		var j = i+1;
		$('#problemas_escolares > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="problemas_escolares_col_'+j+'_1" type="text" class="form-control"/></td></tr>')
	});
	
	var lista_enfermedades_menor = ["Meningitis (Inflamación de las meninges)", "Mareos", "Encefalitis (Inflamación del encéfalo)", "Infecciones ¿Cuáles?", "Fiebres altas", "Problemas digestivos ¿Qué tipo?", "Convulsiones", "Problemas visuales ¿Qué tipo?", "Lesiones en la cabeza ¿En qué zona? -Frontal (En frente), Parietal (Arriba), Occipital (Atrás), Temporal (Lateral)-", "Desmayos", "Caídas ¿De qué tipo?", "Ictericia (Coloración amarillenta debido al aumento de Bilirrubina)", "Fracturas ¿En dónde?", "Hepatitis", "Hospitalizaciones ¿Por qué?", "Eczema o Urticaria (Lesiones rojas en la piel y picazón)", "Operaciones ¿De qué?", "Cáncer ¿Qué tipo?", "Alergias ¿Cuáles?", "Diabetes", "Parálisis ¿De qué miembro?", "VIH", "Problemas auditivos ¿De qué tipo?", "Problemas cardíacos ¿De qué tipo?", "Problemas respiratorios ¿Qué tipo?", "Temblores ¿Dónde?", "Problemas motores ¿De qué tipo?", "Intentos de suicidio ¿Cómo?"];
	$.each( lista_enfermedades_menor, function( i, l ){
		var j = i+1;
		$('#enfermedades_condiciones_menor > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="enfermedades_condiciones_menor_col_'+j+'_1" type="text" class="form-control"/></td><td><input name="enfermedades_condiciones_menor_col_'+j+'_2" type="text" class="form-control"/></td></tr>')
	});
	
	var lista_enfermedades_familiar = ["Cáncer ¿Qué tipo?", "Epilepsia", "Diabetes ¿Qué tipo?", "Infecciones ¿De qué tipo?", "Problemas cardíacos ¿De qué tipo?", "Problemas auditivos ¿De qué tipo?", "Problemas respiratorios ¿De qué tipo?", "Problemas visuales ¿De qué tipo?", "Problemas digestivos ¿De qué tipo?", "Desmayos", "Problemas renales ¿De qué tipo?", "VIH", "Problemas hepáticos ¿De qué tipo?", "Accidente grave ¿De qué tipo?", "Problemas cerebrales ¿De qué tipo?", "Intento de suicidio ¿Cómo?", "Problemas reproductivos ¿De qué tipo?", "Alcoholismo", "Problemas nerviosos ¿De qué tipo?", "Depresión ¿De qué gravedad?", "Problemas emocionales ¿De qué tipo?", "Retraso Mental ¿De qué severidad?", "Problemas motores", "Problemas de aprendizaje", "Derrame cerebral", "Drogadicción", "Parálisis ¿De qué miembro?", "Otros problemas psiquiátricos", "Tabaquismo", "Incapacidad física"];
	$.each( lista_enfermedades_familiar, function( i, l ){
		var j = i+1;
		$('#enfermedades_condiciones_familiar > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="enfermedades_condiciones_familiar_col_'+j+'_1" type="text" class="form-control"/></td><td><input name="enfermedades_condiciones_familiar_col_'+j+'_2" type="text" class="form-control"/></td></tr>')
	});
	
	var lista_conducta_menor = ["Dificultades del habla/lenguaje", "Tiene pesadillas frecuentemente", "Dificultades auditivas", "Tiene problemas de sueño", "Dificultades visuales", "Se da golpes en la cabeza", "Dificultades de coordinación", "Se corta intencionalmente", "Pobre control de esfínteres", "Es demasiado(a) activo(a)", "Pobre control anal", "Es agresivo(a)", "Encopresis (incontinencia fecal; incapaz de retener heces)", "Incontinencia urinaria (Ej. Se orina en la cama)", "Es impulsivo(a)", "Retiene la respiración", "Es torpe a nivel motor (en los movimientos que hace)", "Mece el cuerpo frecuentemente", "Es desatento(a)", "Es temerario(a) (Ej. Realiza conductas extremadamente peligrosas)", "Prefiere estar solo(a)", "No se lleva bien con sus padres", "No se lleva bien con sus hermanos", "No se lleva bien con los compañeros del colegio", "No se lleva bien con sus profesores", "Se come las uñas", "Tiene problemas al comer ¿De qué tipo?", "Es demasiado pasivo(a)", "Llora exageradamente", "Es demasiado enojado(a)", "Se muestra demasiado(a) triste", "Es desobediente e insolente", "Realiza acciones negativas para llamar la atención de los demás", "Ha intentado suicidarse", "Ha hecho daño a animales o personas", "Tiene fuertes temores", "Tiene hábitos extraños ¿Cuáles?", "Hace movimientos extraños ¿De qué tipo? -Cabeza, Cuello, Brazos, Manos, Tronco, Piernas, Pies-", "No establece contacto visual cuando se le habla", "Se da por vencido(a) fácilmente", "Se chupa el dedo", "No quiere ir al colegio", "No quiere hacer tareas", "Se obsesiona con ciertos temas", "Se muestra inflexible"];
	$.each( lista_conducta_menor, function( i, l ){
		var j = i+1;
		$('#conductas_problemas_menor > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="conductas_problemas_menor_col_'+j+'_1" type="text" class="form-control"/></td><td><input name="conductas_problemas_menor_col_'+j+'_2" type="text" class="form-control"/></td></tr>')
	});
	
	var lista_aspectos_padres = ["Comunicación (verbal y no verbal)", "Acuerdo respeto al trato de lo(a)s hijo(a)s", "Capacidad para compartir actividades e interés", "Capacidad para resolver problemas y diferencias", "Situación económica y financiera", "Actividad social", "Satisfacción de necesidades íntimas", "Una red de apoyo dentro de la familia o fuera de la familia", "Compromiso con el rol de padres"];
	$.each( lista_aspectos_padres, function( i, l ){
		var j = i+1;
		$('#aspectos_padres_poseen > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="aspectos_padres_poseen_col_'+j+'_1" type="text" class="form-control"/></td><td><input name="aspectos_padres_poseen_col_'+j+'_2" type="text" class="form-control"/></td><td><input name="aspectos_padres_poseen_col_'+j+'_3" type="text" class="form-control"/></td></tr>')
	});
	
	var lista_tecnica_disciplinaria = ["Ignorar la conducta", "Regañarlo", "Sentarlo(a) en un silla", "Decirle que no lo vuelva a hacer y dejarlo pasar", "Pegarle ¿Cómo?", "Redirigir su interés", "Mandarlo(a) a su cuarto", "Mostrarse enojado(a) con lo que él/ella hizo", "Suprimirle alguna actividad (Ej. Ver televisión, jugar videojuegos, jugar con la computadora, etc.)", "Mostrarse triste con lo que él/ella hizo", "Suprimirle la comida", "Razonar con él", "Gritarle", "Asignarle alguna tarea", "Dejarlo solo para evitar tener que castigarlo", "Tiempo Fuera (ordenarle que se dirija a cierto lugar reservado y durante cierto tiempo, para que se calme y reflexione sobre lo que hizo)"];
	$.each( lista_tecnica_disciplinaria, function( i, l ){
		var j = i+1;
		$('#tecnica_disciplinaria_usada > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="tecnica_disciplinaria_usada_col_'+j+'_1" type="text" class="form-control"/></td></tr>')
	});
	
}
//-------
if($('#nombre_formato').text() == 'Información General de Cliente Adulto'){
	$('#familia_nuclear_adulto > tbody:last-child').append('<tr id="last_line_familia_adulto"><td><input name="familia_nuclear_adulto_1_1" type="text" class="form-control"/></td><td><input name="familia_nuclear_adulto_1_2 type="text" class="form-control"/></td><td><input name="familia_nuclear_adulto_1_3" type="text" class="form-control"/></td><td><input name="familia_nuclear_adulto_1_4" type="text" class="form-control"/></td></tr>');
	function agregar_linea_familia_adulto(){
		var numero = Number($("#filas_familia_nuclear_adulto").val())+1;
		$("#last_line_familia_adulto").unbind();
		$("#last_line_familia_adulto").removeAttr( "id" );
		$('#familia_nuclear_adulto > tbody:last-child').append('<tr id="last_line_familia_adulto"><td><input name="familia_nuclear_adulto_'+numero+'_1" type="text" class="form-control"/></td><td><input name="familia_nuclear_adulto_'+numero+'_2" type="text" class="form-control"/></td><td><input name="familia_nuclear_adulto_'+numero+'_3" type="text" class="form-control"/></td><td><input name="familia_nuclear_adulto_'+numero+'_4" type="text" class="form-control"/></td></tr>');
		$("#filas_familia_nuclear_adulto").val(numero);
		$("#last_line_familia_adulto").on('click', agregar_linea_familia_adulto);
	}
	$("#last_line_familia_adulto").on('click', agregar_linea_familia_adulto);
	
	
	var lista_padecido_problemas = ["Depresión", "Ansiedad", "Intento de Suicidio", "Problema con alcohol", "Problema con drogas", "Problemas mentales", "Problemas emocionales", "Trastornos psicológicos*"];
	$.each( lista_padecido_problemas, function( i, l ){
		var j = i+1;
		$('#familia_padecido_problemas_adulto > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="familia_padecido_problemas_adulto_'+j+'_1" type="text" class="form-control"/></td><td><input name="familia_padecido_problemas_adulto_'+j+'_2" type="text" class="form-control"/></td><td><input name="familia_padecido_problemas_adulto_'+j+'_3" type="text" class="form-control"/></td><td><input name="familia_padecido_problemas_adulto_'+j+'_4" type="text" class="form-control"/></td><td><input name="familia_padecido_problemas_adulto_'+j+'_5" type="text" class="form-control"/></td></tr>')
	});
	
	var lista_padecimiento_adulto = ["Problemas cardíacos", "Diabetes", "Infarto", "Problemas en los riñones", "Problemas en la espalda", "Artritis", "Dolores de cabeza severos", "Presión sanguínea alta", "Falta de aliento", "Incontinencia", "Problemas de sueño", "Sangrado inusual", "Dificultad para dormir", "Heridas en la cabeza", "Desmayos/ Mareos", "Subir/bajar de peso", "Problemas estomacales", "Epilepsia/ Convulsiones", "Asma/ Fiebres altas", "Cambios de humor"];
	$.each( lista_padecimiento_adulto, function( i, l ){
		var j = i+1;
		$('#padecimiento_enfermedad_adulto > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="padecimiento_enfermedad_adulto_'+j+'_1" type="text" class="form-control"/></td></tr>')
	});
	
	
	
	$('#medicamentos_tomando_adulto > tbody:last-child').append('<tr id="last_line_tomando_adulto"><td><input name="medicamentos_tomando_adulto_1_1" type="text" class="form-control"/></td><td><input name="medicamentos_tomando_adulto_1_2" type="text" class="form-control"/></td><td><input name="medicamentos_tomando_adulto_1_3" type="text" class="form-control"/></td></tr>');
	function agregar_linea_tomando_adulto(){
		var numero = Number($("#filas_medicamentos_tomando_adulto").val())+1;
		$("#last_line_tomando_adulto").unbind();
		$("#last_line_tomando_adulto").removeAttr( "id" );
		$('#medicamentos_tomando_adulto > tbody:last-child').append('<tr id="last_line_tomando_adulto"><td><input name="medicamentos_tomando_adulto_'+numero+'_1" type="text" class="form-control"/></td><td><input name="medicamentos_tomando_adulto_'+numero+'_2" type="text" class="form-control"/></td><td><input name="medicamentos_tomando_adulto_'+numero+'_3" type="text" class="form-control"/></td></tr>');
		$("#filas_medicamentos_tomando_adulto").val(numero);
		$("#last_line_tomando_adulto").on('click', agregar_linea_tomando_adulto);
	}
	$("#last_line_tomando_adulto").on('click', agregar_linea_tomando_adulto);
	
	
	$('#info_consulta_recibida_adulto > tbody:last-child').append('<tr id="last_line_consulta_recibida_adulto"><td><input name="info_consulta_recibida_adulto_1_1" type="text" class="form-control"/></td><td><input name="info_consulta_recibida_adulto_1_2" type="text" class="form-control"/></td><td><input name="info_consulta_recibida_adulto_1_3" type="text" class="form-control"/></td></tr>');
	function agregar_linea_consulta_recibida_adulto(){
		var numero = Number($("#filas_info_consulta_recibida_adulto").val())+1;
		$("#last_line_consulta_recibida_adulto").unbind();
		$("#last_line_consulta_recibida_adulto").removeAttr( "id" );
		$('#info_consulta_recibida_adulto > tbody:last-child').append('<tr id="last_line_consulta_recibida_adulto"><td><input name="info_consulta_recibida_adulto_'+numero+'_1" type="text" class="form-control"/></td><td><input name="info_consulta_recibida_adulto_'+numero+'_2" type="text" class="form-control"/></td><td><input name="info_consulta_recibida_adulto_'+numero+'_3" type="text" class="form-control"/></td></tr>');
		$("#filas_info_consulta_recibida_adulto").val(numero);
		$("#last_line_consulta_recibida_adulto").on('click', agregar_linea_consulta_recibida_adulto);
	}
	$("#last_line_consulta_recibida_adulto").on('click', agregar_linea_consulta_recibida_adulto);
	
	
	var lista_problemas_buscar = ["Marital", "Sexual", "Abuso de drogas", "Relaciones personales", "Familiar", "Emocional", "Alcoholismo", "Académico", "Legal", "Financiero", "Trabajo"];
	$.each( lista_problemas_buscar, function( i, l ){
		var j = i+1;
		$('#problematica_buscar_adulto > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="problematica_buscar_adulto_'+j+'_1" type="text" class="form-control"/></td></tr>')
	});
	
	
	$('#info_hospitalizacion_adulto > tbody:last-child').append('<tr id="last_line_hospitalizacion_adulto"><td><input name="info_hospitalizacion_adulto_1_1" type="text" class="form-control"/></td><td><input name="info_hospitalizacion_adulto_1_2" type="text" class="form-control"/></td><td><input name="info_hospitalizacion_adulto_1_3" type="text" class="form-control"/></td></tr>');
	function agregar_linea_hospitalizacion_adulto(){
		var numero = Number($("#filas_info_hospitalizacion_adulto").val())+1;
		$("#last_line_hospitalizacion_adulto").unbind();
		$("#last_line_hospitalizacion_adulto").removeAttr( "id" );
		$('#info_hospitalizacion_adulto > tbody:last-child').append('<tr id="last_line_hospitalizacion_adulto"><td><input name="info_hospitalizacion_adulto_'+numero+'_1" type="text" class="form-control"/></td><td><input name="info_hospitalizacion_adulto_'+numero+'_2'+numero+'" type="text" class="form-control"/></td><td><input name="info_hospitalizacion_adulto_'+numero+'_3" type="text" class="form-control"/></td></tr>');
		$("#filas_info_hospitalizacion_adulto").val(numero);
		$("#last_line_hospitalizacion_adulto").on('click', agregar_linea_hospitalizacion_adulto);
	}
	$("#last_line_hospitalizacion_adulto").on('click', agregar_linea_hospitalizacion_adulto);
}

if($('#nombre_formato').text() == 'Notas de Sesión Inicial en Servicios Clínicos'){
	var lista_areas_disfuncionales = ["Física", "Cognitiva", "Emocional", "Ocupacional", "Familiar", "Social", "Espiritual", "Económica"];
	$.each( lista_areas_disfuncionales, function( i, l ){
		var j = i+1;
		$('#areas_afectadas > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="areas_afectadas_'+j+'_1" type="text" class="form-control"/></td></tr>')
	});
	
	$('#objetivos_estrategias_tratamiento > tbody:last-child').append('<tr id="last_line_estrategias_tratamiento"><td><input name="objetivos_estrategias_tratamiento_1_1" type="text" class="form-control"/></td><td><input name="objetivos_estrategias_tratamiento_1_2" type="text" class="form-control"/></td></tr>');
	function agregar_linea_objetivos_estrategias_tratamiento(){
		var numero = Number($("#filas_objetivos_estrategias_tratamiento").val())+1;
		$("#last_line_estrategias_tratamiento").unbind();
		$("#last_line_estrategias_tratamiento").removeAttr( "id" );
		$('#objetivos_estrategias_tratamiento > tbody:last-child').append('<tr id="last_line_estrategias_tratamiento"><td><input name="objetivos_estrategias_tratamiento_'+numero+'_1" type="text" class="form-control"/></td><td><input name="objetivos_estrategias_tratamiento_'+numero+'_2" type="text" class="form-control"/></td></tr>');
		$("#filas_objetivos_estrategias_tratamiento").val(numero);
		$("#last_line_estrategias_tratamiento").on('click', agregar_linea_objetivos_estrategias_tratamiento);
	}
	$("#last_line_estrategias_tratamiento").on('click', agregar_linea_objetivos_estrategias_tratamiento);
}

if($('#nombre_formato').text() == 'Encuesta de Satisfacción del Cliente en Servicios Clínicos'){
	var lista_nivel_satisfaccion = ["Comunicación telefónica", "Facilidad para concretar una cita", "Cantidad de tiempo que esperó entre la solicitud del servicio y la primera cita", "Calidad del servicio recibido por parte de la secretaria de CIPA", "Grado en que el/la psicólogo(a) en formación mostró cortesía, respeto e interés", "Manera en que el/la psicólogo(a) en formación le escuchó y comprendió", "Habilidades del/la psicólogo(a) en formación al brindarle el/los servicio(s)", "Calidad del/los servicio(s) clínico(s) recibido(s)", "Instalaciones de CIPA", "Tarifa del/los servicio(s) recibido(s)"];
	$.each( lista_nivel_satisfaccion, function( i, l ){
		var j = i+1;
		$('#nivel_satisfaccion > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="nivel_satisfaccion_'+j+'_1" type="text" class="form-control"/></td><td><input name="nivel_satisfaccion_'+j+'_2" type="text" class="form-control"/></td><td><input name="nivel_satisfaccion_'+j+'_3" type="text" class="form-control"/></td><td><input name="nivel_satisfaccion_'+j+'_4" type="text" class="form-control"/></td></tr>')
	});
}

if($('#nombre_formato').text() == 'Encuesta de Satisfacción del Cliente en Servicios Psicoeducativos'){
	var lista_nivel_satisfaccion = ["Comunicación telefónica", "Facilidad para concretar una cita", "Cantidad de tiempo que esperó entre la solicitud del servicio y la primera cita", "Calidad del servicio recibido por parte de la secretaria de CIPA", "Grado en que el/la psicólogo(a) en formación mostró cortesía, respeto e interés", "Manera en que el/la psicólogo(a) en formación le escuchó y comprendió", "Calidad del material que el/la psicólogo(a) en formación le entregó (informes, entre otros)", "Habilidades del/la psicólogo(a) en formación al brindarle el/los servicio(s)", "Calidad del/los servicio(s) psicoeducativo(s) recibido(s)", "Instalaciones de CIPA", "Tarifa del/los servicio(s) recibido(s)"];
	$.each( lista_nivel_satisfaccion, function( i, l ){
		var j = i+1;
		$('#nivel_satisfaccion > tbody:last-child').append('<tr><td>'+l+'</td><td><input name="nivel_satisfaccion_'+j+'_1" type="text" class="form-control"/></td><td><input name="nivel_satisfaccion_'+j+'_2" type="text" class="form-control"/></td><td><input name="nivel_satisfaccion_'+j+'_3" type="text" class="form-control"/></td><td><input name="nivel_satisfaccion_'+j+'_4" type="text" class="form-control"/></td></tr>')
	});
}


if($('#nombre_formato').text() == 'Conceptualización de Caso'){

	$('#hijos_table > tbody:last-child').append('<tr id="last_line_hijos_table"><td><input name="hijos_table_1_1" type="text" class="form-control"/></td><td><input name="hijos_table_1_2" type="text" class="form-control"/></td><td><input name="hijos_table_1_3" type="text" class="form-control"/></td></tr>');
	function agregar_linea_hijos_table(){
		var numero = Number($("#filas_hijos_table").val())+1;
		$("#last_line_hijos_table").unbind();
		$("#last_line_hijos_table").removeAttr( "id" );
		$('#hijos_table > tbody:last-child').append('<tr id="last_line_hijos_table"><td><input name="hijos_table_'+numero+'_1" type="text" class="form-control"/></td><td><input name="hijos_table_'+numero+'_2" type="text" class="form-control"/></td><td><input name="hijos_table_'+numero+'_3" type="text" class="form-control"/></td></tr>');
		$("#filas_hijos_table").val(numero);
		$("#last_line_hijos_table").on('click', agregar_linea_hijos_table);
	}
	$("#last_line_hijos_table").on('click', agregar_linea_hijos_table);
	
	
	$('#familia_table > tbody:last-child').append('<tr id="last_line_familia_table"><td><input name="familia_table_1_1" type="text" class="form-control"/></td><td><input name="familia_table_1_2" type="text" class="form-control"/></td><td><input name="familia_table_1_3" type="text" class="form-control"/></td><td><input name="familia_table_1_4" type="text" class="form-control"/></td><td><input name="familia_table_1_5" type="text" class="form-control"/></td></tr>');
	function agregar_linea_familia_table(){
		var numero = Number($("#filas_familia_table").val())+1;
		$("#last_line_familia_table").unbind();
		$("#last_line_familia_table").removeAttr( "id" );
		$('#familia_table > tbody:last-child').append('<tr id="last_line_familia_table"><td><input name="familia_table_'+numero+'_1" type="text" class="form-control"/></td><td><input name="familia_table_'+numero+'_2" type="text" class="form-control"/></td><td><input name="familia_table_'+numero+'_3" type="text" class="form-control"/></td><td><input name="familia_table_'+numero+'_4" type="text" class="form-control"/></td><td><input name="familia_table_'+numero+'_5" type="text" class="form-control"/></td></tr>');
		$("#filas_familia_table").val(numero);
		$("#last_line_familia_table").on('click', agregar_linea_familia_table);
	}
	$("#last_line_familia_table").on('click', agregar_linea_familia_table);
}
