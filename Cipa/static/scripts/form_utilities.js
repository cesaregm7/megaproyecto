$(function() {
    $( ".date_picker" ).datepicker({
        dateFormat:"dd/mm/yy"
    });
 });
 
$( function() {
    var etiquetasMotivoConsulta = [
      "Trastorno Déficit de Atención",
      "Trastorno Déficit de Atención con Hiperactividad",
      "Autismo",
      "Problemas de Aprendizaje",
      "Déficit Intelectual",
      "Admisión Académica",
      "Habilidad General",
      "Problemas del Habla",
      "Problemas Escolares",
      "Problemas Conductuales",
      "Duelos",
      "Divorcio",
      "Dificultades Familiares",
      "Manejo de Emociones",
      "Relaciones Interpersonales",
      "Trauma",
      "Trastornos del Desarrollo",
      "Trastorno Degenerativo",
      "Anoxia",
      "Epilepsia",
      "Depresión",
      "Ansiedad",
      "Trastorno Obsesivo Compulsivo",
      "Trastornos Alimentarios",
      "Trastorno de la Personalidad",
      "OTROS"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#id_consultation_reason" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetasMotivoConsulta, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  $( function() {
    var etiquetasDiagnostico = [
      "------Discapacidad Intelectual------","Discapacidad Intelectual Leve","Discapacidad Intelectual Moderado","Discapacidad Intelectual Grave","Discapacidad Intelectual Profundo",
      "Retraso General del Desarrollo",
      "------Trastornos de la Comunicación------","Trastorno del Lenguaje", "Trastornos Fonológico", "Trastorno de Fluidez (Tartamudeo)",
      "Autismo",
      "Trastorno Déficit de Atención",
      "Trastorno Déficit de Atención con Hiperactividad",
      "------Trastorno Específico del Aprendizaje------","Dislexia", "Disgrafia", "Discalculia",
      "------Trastornos Motores------","Trastornos del desarrollo de la coordinación", "Trastornos de Movimientos Estereotipados", "Trastornos de la Tourette", "Trastornos de Tics motores o vocales", "Trastornos de Tic transitorio",
      "------Esquizofrenia y otros Trastornos Psicóticos------","Trastorno Esquizotípico de la personalidad", "Trastorno de Delirios", "Trastorno Esquizofreniforme", "Esquizofrenia", "Trastorno Esquizoafectivo", "Trastorno Psicótico inducido por sustancias", "Trastorno Psicótico por afección médica",
      "------Trastorno Bipolar------","Trastorno Bipolar  I", "Trastorno Bipolar II", "Trastorno Ciclotímico",
      "------Trastornos Depresivos------","Trastorno de Depresión Mayor", "Distimia", "Trastorno Disfórico Premenstrual", 
      "------Trastornos de Ansiedad------","Trastorno de Ansiedad por Separación", "Mutismo Selectivo", "Fobia Específica", "Fobia Social", "Trastorno de Pánico", "Agorafobia","Trastorno de ansiedad generalizada",
      "------Trastorno Obsesivo Compulsivo------","Trastorno Dismórfico Corporal", "Trastorno de Acumulación", "Tricotilomanía", "Trastorno de excoriación",
      "------Trastorno Relacionado con Trauma------","Trastorno de Apego Reactivo", "Trastorno de relación social desinhibida", "Trastorno de Estrés Postraumático", "Trastorno de Estrés Agudo",
      "------Trastornos de Síntomas Somáticos------","Trastorno de ansiedad por enfermedad", "Trastorno Facticio",
      "------Trastornos Alimentarios y de Ingestión de Alimentos------","Pica","Trastorno de rumiación","Trastorno de restricción de ingesta de alimentos", "Anorexia Nerviosa", "Bulimia Nerviosa", "Trastorno por Atracón",
      "------Trastorno de la Excresión------","Enuresis", "Encopresis",
      "------Trastornos del Sueño-Vigilia------","Trastorno de Insomnio", "Trastorno por Hipersomnia", "Narcolepsia",
      "------Trastornos destructivos, del control de impulsos y de la conducta------","Trastorno negativista desafiante", "Trastorno explosivo intermitente", "Trastorno de personalidad antisocial", "Piromanía", "Cleptomanía",
      "------Trastornos adictivos------","Trastorno por consumo de alcohol", "Trastorno por consumo de cannabis", "Trastorno por consumo de fenciclidina", "Trastorno por sedantes, hipnóticos o ansiolíticos",
      "------Trastornos de la personalidad------","paranoide", "esquizoide", "esquizotípica", "antisocial", "límite", "histriónica", "narcicistia", "evasiva", "dependiente", "obsesivo-compulsivo",
      "------Trastornos Parafílicos------","Trastorno de Voyeurismo", "Trastorno de exhibicionismo", "Trastorno de froteurismo", "Trastorno de masoquismo sexual", "Trastorno de sadismo sexual", "Trastorno de pedofilia", "Trastorno de fetichismo",
      "Negligencia",
      "Maltrato",
      "Abuso Sexual",
      "Problemas económicos",
      "Pruebas de Admisión",
      "Problemas Escolares",
      "Habilidad General",
      "Problemas del Habla",
      "Problemas Conductuales",
      "Duelos",
      "Divorcio",
      "Dificultades Familiares",
      "Manejo de Emociones",
      "Relaciones Interpersonales",
      "Trauma",
      "Trastorno Autoinmunológico",
      "Trastornos del Desarrollo",
      "Trastornos Degenerativos",
      "Trastornos por Deficiencias Nutricionales",
      "Trastornos por Toxicidad",
      "Tumores",
      "Accidentes Cerebrovasculares",
      "Anoxia",
      "Epilepsia",
      "Hidrocefalia",
      "Trastornos Infecciosos",
      "Metabólicos",
      "OTROS"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#id_diagnosis" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetasDiagnostico, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
 $( function() {
    var etiquetasPruebasAplicadas = [
      "------Pruebas de Habilidades Generales------", "Differential Aptitude Scale (DAS)", "Test Breve de Inteligencia Kaufman (K.BIT)", "Stanford-Binet Intelligence Scale (Stanford-Binet)", "Escala de Inteligencia de Wechsler para adultos (WAIS)", "Escala de Inteligencia de Wechsler para Adultos (WAIS)", "Escala de Inteligencia Wechsler para Adultos (EIWA)", "Escala de Inteligencia Wechsler para Adultos (WAIS-IV)", "Escala de Inteligencia de Wechsler para Niños (WISC-R)", "Escala Wechsler de Inteligencia para Niños (WISC-III)", "Escala de Inteligencia Wechsler para Niños (WISC-IV)", "Escala de Inteligencia de Wechsler para Preescolares(WPPSI-III)", "Escala de inteligencia de Wechsler para pre escolares (WPPSI-R)", "Escala de Inteligencia para los niveles pre escolares y primarios (WPPSI)", "Columbia Mental Maturity Scale (CMMS)", "Boehm Test of Basic Concepts (Boehm-3)", "Culture Fair Intelligence Test (Factor G)", "Escala McCarthy de Aptitudes y Psicomotricidad para Niños (MSCA)", "Batería de Evaluación de niños Kaufman (K.ABC)", "Aptitudes Mentales Primarias (PMA)", "Aptitudes Básicas Generales (ABG-1)", "Aptitudes Básicas Generales 2 (ABG-2)",
      "------Pruebas de Habilidades Generales sin la Influencia del Lenguaje (No Verbales)------", "Escala Manipulativa Internacional (Leiter-R)", "Escala de Inteligencia No Verbal (TONI-2)",
      "------Pruebas de Habilidades/Procesos Cognitivos------", "Woodcock-Johnson III Prueba de Habilidades Cognitivas (WJ-III Cognitivo)", "Test of Cognitive Abilities Woodcock-Johnson III (WJ-III Cognitivo INGLÉS)", "Woodcock-Johnson III Normative Update (WJ-III NU)", "Pruebas de Habilidades Cognitivas Revisada Woodcock-Muñoz (WM-R Cognitivo)", "Cognitive Assessment System (CAS)", "Cognitive Assessment System 2 (CAS 2)", "Delis-Kaplan Executive Function System (D-KEFS)", "Behavior Rating, Inventory of Executive Function (BRIEF)", "Test Factorial de Inteligencia (AMPE-F)", "Inteligencia General Factorial (IGF)", "Test de Inteligencia Creativa (CREA)",
      "------Pruebas de Aprovechamiento------", "Prueba de Aprovechamiento de Woodcock-Johnson Batería III (WJ-III Aprovechamiento)", "Prueba de Aprovechamiento de Woodcock –Muñoz Revisada (WM-R Aprovechamiento)", "Bracken Basic Concept Scale-Revised (Bracken)", "Kaufman Test of Educational Achievement (K-TEA)",
      "------Pruebas de Viso Motricidad------", "Prueba del Desarrollo de la Integración Viso Motriz (VMI)", "Koppitz Developmental Scoring System for the Bender Gestalt Test (Koppitz-2)",
      "------Pruebas de Atención------", "Test de Atención d2 (d2)", "Test de Evaluación del Trastorno por Déficit de Atención con Hiperactividad (EDAH)",
      "------Pruebas de Memoria------", "Wechsler Memory Scale III (WMS-III)", "Test of Memory and Learning (TOMAL)",
      "------Pruebas de Lectura y Lenguaje------", "Batería de Evaluación de los Procesos Lectores – Revisada (PROLEC-R)", "Expressive One-Word", "Test de Vocabulario en Imágenes Peabody", "Batería de evaluación de los procesos lectores en alumnos de tercer ciclo de educación y educación secundaria obligatoria (PROLEC-SE)", "Test of Phonological awareness in Spanish (TPAS)",
      "------Pruebas de Personalidad------", "Cuestionario de 90 síntomas (SCL-90- R)", "Children’s Personality Questionnaire (CPQ)", "Cuestionario Factorial de Personalidad (16 PF-5)", "Inventario Clínico Multiaxial de Millon III (MCMI-III)", "Test de Inteligencia Emocional Mayer-Salovey- Caruso (MSCEIT)", "Escala de adjetivos interpersonales (IAS)", "Inventario diferencial de adjetivos para la evaluación del estado de ánimo (IDDA-EA)", "Cuestionario Big Five (BFQ)", "Minnesota Multiphasic Inventory 2 (MMPI-2- RF)", "Listado de Síntomas Breve (LSB-50)", "Eysenck Personality Questionnaire (EPQ-R)", "Escala de Ansiedad Manifestada en Niños (CMAS-R)", "Cuestionario de Ansiedad Infantil (CAS)",
      "------Pruebas Proyectivas------", "Test de la Familia", "Test del Árbol", "Test de Apercepción Infantil (CAT-H)", "Test de Patte Noire", "Test de SZONDI", "Test de Apercepción Temática (TAT)", "Draw a person: Screening Procedure for Emotional Disturbance (DAP:SPED)",
      "------Pruebas de Evaluación del Desarrollo------", "Bayley Scale Of Infant Development II edition", "Bayley Scale Of Infant Development - II edition. Motor Scale Test KIT", "Ages &amp; Stages Questionnaires en Español", "Inventario de Desarrollo BATELLE",
      "------Pruebas Neuropsicológicas------", "Behavioral Inattention Test", "Adaptive Behavior Assessment System II", "Cuestionario de Madurez Neuropsicológica Infantil", "Evaluación Neuropsicológica Breve en Español", "Entrevista para el diagnóstico del Autismo", "Test de Homogeneidad y Preferencia Lateral",
      "------Inventario y Hábitos de Estudio------", "Cuestionario de hábitos y técnicas de estudio", "Instrucciones Complejas",
      "------Inventario de Aptitudes Primarias (Valores)------", "Monedas: Aptitud de tipo superior (Niveles 1 y 2)", "Comprensión de órdenes escritas Niveles 1, 2, y 3", "Cuestionario de valores personales", "Survey of Interpersonal Values",
      "------Pruebas Psicología Organizacional------", "Cuestionario de Clima Laboral", "Batería de test para la selección de personal administrativo –I", "Test de aptitudes administrativas -I [a]", "CompeTEA", "Cuestionario de estrés laboral", "Inventario de personalidad para vendedores", "Test de aptitudes administrativas", "Baterías de tareas administrativas",
      "------Pruebas de Escolaridad------", "Temas de educación para la salud", "Diagnóstico Integral de Estudio",
      "------Programas------", "Programa para mejorar la convivencia escolar Programa para mejorar la convivencia escolar", "Programa para mejorar la convivencia escolar", "Programa ABC Dislexia",
      "------Intereses------", "Intereses preferencias profesionales",
      "------Acoso y Convivencia Escola------", "Acoso y Violencia Escolar","Batería de Socialización 1 y 2", "Batería de Socialización 3"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#id_applied_tests" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetasPruebasAplicadas, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  
/*----------Auto complete Juegos-----------*/
$( function() {
    var etiquetas_subjetivo_feliz = [
      "FELIZ", "aliviado", "satisfecho", "complacido", "emocionado", "sorprendido", "encantado", "tonto"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#subjetivo_feliz" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_subjetivo_feliz, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  $( function() {
    var etiquetas_subjetivo_confiado = [
      "CONFIADO", "orgulloso", "fuerte", "poderoso", "determinado", "libre"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#subjetivo_confiado" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_subjetivo_confiado, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_subjetivo_triste = [
      "TRISTE", "decepcionado", "sin esperanza", "pesimista", "desalentado", "solo"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#subjetivo_triste" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_subjetivo_triste, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  
  $( function() {
    var etiquetas_subjetivo_vacilante = [
      "VACILANTE", "tímido", "confundido", "nervioso", "avergonzado", "desconcertado"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#subjetivo_vacilante" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_subjetivo_vacilante, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_subjetivo_enojado = [
      "ENOJADO", "impaciente", "molesto", "frustrado", "enojado", "ruin", "celoso"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#subjetivo_enojado" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_subjetivo_enojado, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  
  $( function() {
    var etiquetas_subjetivo_curioso = [
      "CURIOSO", "interesado", "enfocado"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#subjetivo_curioso" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_subjetivo_curioso, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_subjetivo_miedoso = [
      "MIEDOSO", "vulnerable", "impotente", "desconfiado", "ansioso", "temeroso", "espantado", "aterrorizado"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#subjetivo_miedoso" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_subjetivo_miedoso, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_subjetivo_superficial = [
      "SUPERFICIAL","contenido", "ambiguo", "restringido"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#subjetivo_superficial" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_subjetivo_superficial, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  
  $( function() {
    var etiquetas_objetivo_juguetes = [
      "martillo","reglas","tablas","carpintería",
      "arenero","agua","lavado",
      "teatro","títeres",
      "cocina","cocinar","comida",
      "caballete","pinturas","pizarrón",
      "bean bag","almohadas","frazada","sábana",
      "bob bag","bates de esponja",
      "disfrazarse:ropa", "disfrazarse:telas", "disfrazarse:zapatos", "disfrazarse:joyas", "disfrazarse:sombreros", "disfrazarse:máscaras", "disfrazarse:varita mágica",
      "artesanías","plasticina","marcadores",
      "casa de muñecas","familia","biberón","chupete","bebe",
      "máquina registradora","dinero","teléfono",
      "cámara","linterna",
      "kit médico","vendajes",
      "instrumentos musicales",
      "juegos","boliche","pelotas","lanzamiento de aros",
      "carros","camiones","bus","vehículos para emergencias","aviones","lanchas","carruaje",
      "animales domésticos","zoológico","lagarto","dinosaurios","tiburón","serpiente",
      "soldados","pistolas","cuchillo","espadas","esposas","cuerda",
      "juguetes constructivos","trozos","barricadas",
      "azafate con arena","miniaturas"
      
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#objetivo_juguetes" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_objetivo_juguetes, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_motivo_del_límite = [
      "Proteger al niño (seguridad física y emocional)","Proteger al terapeuta y/o mantener la aceptación y relación terapéutica", "Proteger los juguetes y el salón de juegos", "Estructurar", "Evaluación de la realidad"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#motivo_del_límite" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_motivo_del_límite, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_juego_exploratorio_lista = [
      "EXPLORATORIO","adapta","familiariza"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_exploratorio_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_exploratorio_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
    
  
  $( function() {
    var etiquetas_juego_relacional_lista = [
      "RELACIONAL","conexión","confianza","búsqueda de aprobación","manipulador","colaborador","prueba"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_relacional_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_relacional_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_juego_poder_lista = [
      "PODER","CONTROL"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_poder_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_poder_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  
  $( function() {
    var etiquetas_juego_inadecuado_lista = [
      "INADECUADO","IMPOTENCIA"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_inadecuado_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_inadecuado_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_juego_agresion_lista = [
      "AGRESIÓN","VENGANZA"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_agresion_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_agresion_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  $( function() {
    var etiquetas_juego_seguridad_lista = [
      "SEGURIDAD","PROTECCIÓN"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_seguridad_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_seguridad_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_juego_dominio_lista = [
      "DOMINIO","construir","competencia","integración"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_dominio_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_dominio_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  
  $( function() {
    var etiquetas_juego_cuidado_lista = [
      "CUIDADO (NURTURING)","autocuidado","reparación","sanación"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_cuidado_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_cuidado_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_juego_muerte_lista = [
      "MUERTE","PÉRDIDA","DUELO"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#juego_muerte_lista" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_juego_muerte_lista, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
  
  $( function() {
    var etiquetas_evaluacion_plan = [
      "Consulta con los padres","Sesión familiar","Sesión con hermanos", "Recurrir a un amigo/a", "Terapia filial (juego en casa grabado y discutido en sesión siguiente)", "Terapia para los padres", "Recursos recomendados para los padres", "Medicamentos, Evaluación", "Evaluación psicológica", "Consulta en establecimiento educativo", "Observación en clase", "Consulta con profesional: Psiquiatra, pediatra, abogado", "Solicitud de Récords", "Otros planes y recomendaciones"
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
 
    $( "#evaluacion_plan" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            etiquetas_evaluacion_plan, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
  
 
