class CoelhosController:

    def run(self, coelhos):
        
        if coelhos is None:
            raise Exception("Defina a lista de coelhos")
        
        coelho_stack = []
        multa = 0    
        current_coelho = (0,0)
        for coelho in coelhos:
            # if current_coelho is None:
            #     current_coelho = coelho
            # else:
            #     coelho_stack.append(coelho)
            
            coelho_stack.append(coelho)
            
            if current_coelho[0] == 0:
                current_coelho = self.decision(coelho_stack)
                coelho_stack.remove(current_coelho)
                
            current_coelho[0] -= 1
            multa += self.calc_multa(coelho_stack)
        
        while(coelho_stack):
            if current_coelho[0] == 0:
                current_coelho = self.decision(coelho_stack)
                coelho_stack.remove(current_coelho)
                
            current_coelho[0] -= 1
            multa += self.calc_multa(coelho_stack)
        
        return multa
    
    def decision(self, stack):
        best = stack[0]
        
        for coelho in stack:
            best_count = float(best[1]) / best[0]
            razao = float(coelho[1]) / coelho[0]
            if razao > best_count:
                best = coelho
        
        return best
    
    def calc_multa(self, stack):
        _multa = 0
        for coelho in stack:
            _multa += self.calc_multa_coelho(coelho)
        return _multa
    
    def calc_multa_coelho(self, coelho):
        return coelho[1]

            
        
            
            