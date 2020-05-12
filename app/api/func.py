class validation_function:

    
    def check_valid(self,value,constraint,var_name):
        if constraint == None:
            return True
        else:
            try:
                x = value
                y = eval(constraint,{var_name : x})
                return y 
            except:
                return False

    def validate_numeric_entity(self,values,invalid_trigger,key,support_multiple,pick_first,constraint,var_name):
        pick_first = False
        filled = True 
        partially_filled = False
        trigger = ''
        parametres = {}
        accepted_ages = []

        if len(values) == 0:     # Case of no input given
            filled = False 
            partially_filled = False 
            trigger = invalid_trigger
        else:
            index = 0 
            for dict_values in values:
                validity = self.check_valid(self,dict_values["value"],constraint,var_name)   # Check input validity
                if validity==False:
                    filled = False 
                    partially_filled = True 
                    trigger = invalid_trigger
                     
                else:
                    accepted_ages.append(dict_values["value"])
                if index == 0:
                    if validity:
                        pick_first = True    
                index += 1 

        if len(accepted_ages) != 0  and len(values) != 0:    # result oriented approach (Faulty to me)
            parametres = accepted_ages[0]               
                

        # ........What should have been the approach.......
        
        # if len(accepted_ages) > 1 and len(values) != 0:
        #     if support_multiple == True:                # Only if reuse set to true, it will support all the valid values
        #         parametres = accepted_ages
        #     else:
        #         parametres = accepted_ages[0]
        # elif len(accepted_ages) == 1 and len(values) != 0:
        #     parametres = accepted_ages[0]

        SlotValidationResult = {}                           # Computing Final Result
        SlotValidationResult['filled'] = filled
        SlotValidationResult['partially_filled'] = partially_filled
        SlotValidationResult['trigger'] = trigger 
        if parametres == {}:
            SlotValidationResult['parametres'] = parametres
        else:
            SlotValidationResult['parametres'] = {key : parametres}

        return SlotValidationResult
