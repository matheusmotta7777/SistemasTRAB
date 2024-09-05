# import time

# x1 = 0 
# x2 = 0
# x3 = 0
# x4 = 0

# class VM:
#     def __init__(self, ID, VCPU, EXECTIME, ARRIVTIME, PRIORITY):
#         self.ID = ID
#         self.VCPU = VCPU
#         self.EXECTIME = EXECTIME
#         self.ARRIVTIME = ARRIVTIME
#         self.PRIORITY = PRIORITY


# VM1 = VM("VM1", 2, 20, 40, 2 )
# VM2 = VM("VM2", 1, 25, 15, 2)
# VM3 = VM("VM3", 4, 5, 50, 2)
# VM4 = VM("VM4", 4, 25, 15, 0)
# VM5 = VM("VM5", 2, 35, 45, 0)
# VM6 = VM("VM6", 4, 30, 25, 3)
# VM7 = VM("VM7", 1, 30, 45, 0)
# VM8 = VM("VM8", 1, 10, 40, 0)
# VM9 = VM("VM9", 2, 20, 5, 3)
# VM10 = VM("VM10", 1, 5, 20, 1)

# inicio_x1 = None
# inicio_x2 = None
# inicio_x3 = None
# inicio_x4 = None

# for i in range(90):
#     print(f"{i+1} segundos // ({x1}) ({x2}) ({x3}) ({x4})")
#     # if (i + 1) % 1 == 1:
#         # x1 += 1
    
#     if i == 3:  # sempre colocar dois segundo a menos do que o q vc quiser
#         x1 = VM9.ID
#         x2 = VM9.ID
#         inicio_x1 = i
#         inicio_x2 = i
    
#     if inicio_x1 is not None and (i -  inicio_x1) >= VM9.EXECTIME:
#         x1 = 0
#     if inicio_x2 is not None and (i -  inicio_x2) >= VM9.EXECTIME:
#         x2 = 0



#         x3 = VM1.ID
#         x4 = VM1.ID
#         inicio_x3 = i
#         inicio_x4 = i
    
#     if inicio_x3 is not None and (i -  inicio_x3) >= VM1.EXECTIME:
#         x3 = 0
#     if inicio_x4 is not None and (i -  inicio_x4) >= VM1.EXECTIME:
#         x4 = 0
#         time.sleep(0)

import time

slots = [0, 0, 0, 0]

class VM:
    def __init__(self, ID, VCPU, EXECTIME, ARRIVTIME, PRIORITY):
        self.ID = ID
        self.VCPU = VCPU
        self.EXECTIME = EXECTIME
        self.ARRIVTIME = ARRIVTIME
        self.PRIORITY = PRIORITY

vms = [
    VM("VM1", 2, 20, 40, 2),
    VM("VM2", 1, 25, 15, 2),
    VM("VM3", 4, 5, 50, 2),
    VM("VM4", 4, 25, 15, 0),
    VM("VM5", 2, 35, 45, 0),
    VM("VM6", 4, 30, 25, 3),
    VM("VM7", 1, 30, 45, 0),
    VM("VM8", 1, 10, 40, 0),
    VM("VM9", 2, 20, 5, 3),
    VM("VM10", 1, 5, 20, 1)
]

# Ordena pela PRIORITY (menor prioridade primeiro) e depois por ARRIVTIME
vms.sort(key=lambda vm: (vm.PRIORITY, vm.ARRIVTIME))

# Dicionário para armazenar o início de execução de cada VM
inicio_vm = {}

# Função para verificar se há slots disponíveis para a VM
def alocar_slots(vm):
    slots_livres = [i for i in range(len(slots)) if slots[i] == 0]  # Encontra slots livres
    if len(slots_livres) >= vm.VCPU:  # Verifica se há slots suficientes para a VM
        for i in range(vm.VCPU):
            slots[slots_livres[i]] = vm.ID  # Aloca os slots para a VM
        return True
    return False

# Função para liberar os slots de uma VM após a execução
def liberar_slots(vm):
    for i in range(len(slots)):
        if slots[i] == vm.ID:
            slots[i] = 0  # Libera o slot

for i in range(90):
    # Exibe o estado dos slots no formato (x1) (x2) (x3) (x4)
    print(f"{i+1} segundos // ({slots[0]}) ({slots[1]}) ({slots[2]}) ({slots[3]})")

    for vm in vms:
        # Iniciar a VM se o tempo atual for >= ARRIVTIME e ela não tiver sido iniciada
        if vm.ID not in inicio_vm and i >= vm.ARRIVTIME:
            if alocar_slots(vm):  # Tenta alocar slots para a VM
                inicio_vm[vm.ID] = i  # Marca o tempo de início da VM

    # Verifica o tempo de execução de cada VM e libera os slots quando a execução termina
    for vm in vms:
        if vm.ID in inicio_vm:
            inicio_execucao = inicio_vm[vm.ID]
            if i - inicio_execucao >= vm.EXECTIME:
                liberar_slots(vm)  # Libera os slots após o término da execução

    time.sleep(1)

