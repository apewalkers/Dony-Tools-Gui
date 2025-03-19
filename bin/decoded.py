def err_code(err_code):
    msg = 'Unknown - REPORT'
    if err_code[0:8] == '80000001':
        msg = 'Failed to access thermal sensor '
    elif err_code[0:8] == '80000004':
        msg = 'AC/DC Power Fail                     '
    elif err_code[0:8] == '80000005':
        msg = 'Main SoC CPU Power Fail             '
    elif err_code[0:8] == '80000006':
        msg = 'Main SoC GFX Power Fail             '
    elif err_code[0:8] == '80000007':
        msg = 'Main SoC Thrm Hi Tempr Abnormal '
    elif err_code[0:8] == '80000008':
        msg = 'Drive Dead Notify Timeout             '
    elif err_code[0:8] == '80000009':
        msg = 'AC In Detect                         '
    elif err_code[0:8] == '8000000A':
        msg = 'VRM HOT Fatal                         '
    elif err_code[0:8] == '8000000B':
        msg = 'Unexpected Thermal Shutdown         '
    elif err_code[0:8] == '8000000C':
        msg = 'MSoC Tempr Alert                     '
    elif err_code[0:8] == '80050000':
        msg = 'SoC VRM Power Fail (CPU)            '
    elif err_code[0:4] == '8005':
        msg = 'SoC VRM Power Fail (CPU)            '
    elif err_code[0:8] == '80060000':
        msg = 'SoC VRM Power Fail (GFX)            '
    elif err_code[0:4] == '8006':
        msg = 'SoC VRM Power Fail (GFX)            '
    elif err_code[0:4] == '8080':
        msg = 'Fatal Shutdown by OS request         '
    elif err_code[0:8] == '80810001':
        msg = 'Power Seq Error                     '
    elif err_code[0:8] == '80810002':
        msg = 'Power Seq: NVS Access Error         '
    elif err_code[0:8] == '80810013':
        msg = 'Power Seq: ScCmd DRAM Init Error'
    elif err_code[0:8] == '80810014':
        msg = 'Power Seq: ScCmd Link Up Failure'
    elif err_code[0:8] == '80830000':
        msg = 'Main SoC Sync Flood                 '
    elif err_code[0:8] == '80840000':
        msg = 'PCIe Link Down                         '
    elif err_code[0:8] == '80870001':
        msg = 'Flash Cont:RAM Protect Error         '
    elif err_code[0:8] == '80870002':
        msg = 'Flash Cont:RAM Parity Error         '
    elif err_code[0:8] == '80870003':
        msg = 'Flash Cont:Boot Failed                 '
    elif err_code[0:8] == '80870004':
        msg = 'Flash Cont:Boot Failed NoRecord '
    elif err_code[0:8] == '80870005':
        msg = 'Flash Cont:Boot Failed State Err'
    elif err_code[0:6] == '808710':
        msg = 'Flash Cont:ScCmd Response Error     '
    elif err_code[0:4] == '8088':
        msg = 'Flash Cont:Boot EAP Error             '
    elif err_code[0:4] == '8089':
        msg = 'Flash Cont:Boot EFC Error             '
    elif err_code[0:4] == '808A':
        msg = 'Flash Cont:Temper Error             '
    elif err_code[0:4] == '808B':
        msg = 'Flash Cont:Watch Dog Timer            '
    elif err_code[0:4] == '808C':
        msg = 'USB Type-C Errror                     '
    elif err_code[0:8] == '808D0000':
        msg = 'Thermal Shutdown: Main SoC         '
    elif err_code[0:8] == '808D0001':
        msg = 'Thermal Shutdown: Local Sensor 1'
    elif err_code[0:8] == '808D0002':
        msg = 'Thermal Shutdown: Local Sensor 2'
    elif err_code[0:8] == '808D0003':
        msg = 'Thermal Shutdown: Local Sensor 3'
    elif err_code[0:8] == '808E0000':
        msg = 'COM Err:Close Error                 '
    elif err_code[0:8] == '808E0001':
        msg = 'COM Err:Open Error                     '
    elif err_code[0:8] == '808E0002':
        msg = 'COM Err:Host Write Flag Error     '
    elif err_code[0:8] == '808E0003':
        msg = 'COM Err:EMC Read Flag Error         '
    elif err_code[0:8] == '808E0004':
        msg = 'COM Err:Write Flag Error             '
    elif err_code[0:8] == '808E0005':
        msg = 'COM Err:Wait SIG1 Error             '
    elif err_code[0:8] == '808E0006':
        msg = 'COM Err:Reset request from Host     '
    elif err_code[0:8] == '808E0007':
        msg = 'COM Err:Checksum Error             '
    elif err_code[0:8] == '808F0001':
        msg = 'SMCU Com Err:Timeout                 '
    elif err_code[0:8] == '808F0002':
        msg = 'SMCU Com Err:Reset                     '
    elif err_code[0:8] == '808F0003':
        msg = 'SMCU Com Err:TIS Error             '
    elif err_code[0:8] == '808F00FF':
        msg = 'SMCU Com Err:Undefined             '
    elif err_code[0:4] == '8090':
        msg = 'Fatal Shutdown by Error Add Code'
    elif err_code[0:4] == '8091':
        msg = 'SSD PMIC Error                         '
    elif err_code[0:8] == '80C00114':
        msg = 'Watch Dog For SoC                     '
    elif err_code[0:8] == '80C00115':
        msg = 'Watch Dog For EAP                     '
    elif err_code[0:8] == '80C0012C':
        msg = 'BD Drive Detached                     '
    elif err_code[0:8] == '80C0012D':
        msg = 'EMC Watch Dog Timer Error             '
    elif err_code[0:8] == '80C0012E':
        msg = 'ADC Error (Button)                     '
    elif err_code[0:8] == '80C0012F':
        msg = 'ADC Error (BD Drive)                 '
    elif err_code[0:8] == '80C00130':
        msg = 'ADC Error (AC In Det)                 '
    elif err_code[0:8] == '80C00131':
        msg = 'USB Over Current                     '
    elif err_code[0:8] == '80C00132':
        msg = 'FAN Storage Access Failed             '
    elif err_code[0:8] == '80C00133':
        msg = 'USB-BT FW Header Invalid             '
    elif err_code[0:8] == '80C00134':
        msg = 'USB-BT BT Command Error             '
    elif err_code[0:8] == '80C00135':
        msg = 'USB-BT Memory Malloc Failed         '
    elif err_code[0:8] == '80C00136':
        msg = 'USB-BT Device Not Found             '
    elif err_code[0:8] == '80C00137':
        msg = 'USB-BT MISC Error                     '
    elif err_code[0:8] == '80C00138':
        msg = 'Flash Cont Interrupt HW Error     '
    elif err_code[0:8] == '80C00139':
        msg = 'BD Drive Eject Assert Delayed         '
    elif err_code[0:6] == '80D001':
        msg = 'USB-BT Error (Bulk Out)             '
    elif err_code[0:6] == '80D002':
        msg = 'USB-BT Error (Bulk In)             '
    elif err_code[0:6] == '80D003':
        msg = 'USB-BT Error (Bt Init)             '
    elif err_code[0:6] == '80D004':
        msg = 'USB-BT Error (Download Firmware)'
    elif err_code[0:6] == '80D005':
        msg = 'USB-BT Error (Release Device)         '
    elif err_code[0:6] == '80D006':
        msg = 'USB-BT Error (Exec Cmd0)             '
    elif err_code[0:6] == '80D007':
        msg = 'USB-BT Error (Exec Cmd1)             '
    elif err_code[0:2] == 'B0':
        msg = 'Sonics Bus Error                     '
    elif err_code[0:4] == 'C001':
        msg = 'Main SoC Access Error (I2C)         '
    elif err_code[0:4] == 'C002':
        msg = 'Main SoC Access Err (SB-TSI I2C)'
    elif err_code[0:4] == 'C003':
        msg = 'Main SoC Access Error (SB-RMI)     '
    elif err_code[0:4] == 'C00B':
        msg = 'Serial Flash Access Error             '
    elif err_code[0:4] == 'C00C':
        msg = 'VRM Controller Access Error         '
    elif err_code[0:4] == 'C00D':
        msg = 'PMIC (Subsystem) Access Error         '
    elif err_code[0:4] == 'C010':
        msg = 'Flash Controller Access Error     '
    elif err_code[0:4] == 'C011':
        msg = 'Potentiometer Access Error         '
    elif err_code[0:4] == 'C015':
        msg = 'PCIe Redriver Access Errror         '
    elif err_code[0:4] == 'C016':
        msg = 'PMIC (SSD) Access Error             '
    elif err_code[0:4] == 'C081':
        msg = 'HDMI Tx Access Error                 '
    elif err_code[0:4] == 'C090':
        msg = 'USB Type-C PD Cont Access Error '
    elif err_code[0:4] == 'C091':
        msg = 'USB Type-C USB/DP Mux Accss Err '
    elif err_code[0:4] == 'C092':
        msg = 'USB Type-C Redriver Access Error'
    elif err_code[0:4] == 'C0FE':
        msg = 'Dummy                                 '
    elif err_code[0:8] == '80C00140':
        msg = 'MAIN_SOC - FORCE OFF                     '

    #################

    elif err_code[0:8] == '80801101':
        msg = 'RAM GDDR6 1'
    elif err_code[0:8] == '80801102':
        msg = 'RAM GDDR6 2'
    elif err_code[0:8] == '80801103':
        msg = 'RAM GDDR6 1 2'
    elif err_code[0:8] == '80801104':
        msg = 'RAM GDDR6 3'
    elif err_code[0:8] == '80801105':
        msg = 'RAM GDDR6 1 3'
    elif err_code[0:8] == '80801106':
        msg = 'RAM GDDR6 2 3'
    elif err_code[0:8] == '80801107':
        msg = 'RAM GDDR6 1 2 3'
    elif err_code[0:8] == '80801108':
        msg = 'RAM GDDR6 4'
    elif err_code[0:8] == '80801109':
        msg = 'RAM GDDR6 1 4'
    elif err_code[0:8] == '8080110A':
        msg = 'RAM GDDR6 2 4'
    elif err_code[0:8] == '8080110B':
        msg = 'RAM GDDR6 1 2 4'
    elif err_code[0:8] == '8080110C':
        msg = 'RAM GDDR6 3 4'
    elif err_code[0:8] == '8080110D':
        msg = 'RAM GDDR6 1 3 4'
    elif err_code[0:8] == '8080110E':
        msg = 'RAM GDDR6 2 3 4'
    elif err_code[0:8] == '8080110F':
        msg = 'RAM GDDR6 1 2 3 4'
    elif err_code[0:8] == '80801110':
        msg = 'RAM GDDR6 5'
    elif err_code[0:8] == '80801111':
        msg = 'RAM GDDR6 1 5'
    elif err_code[0:8] == '80801112':
        msg = 'RAM GDDR6 2 5'
    elif err_code[0:8] == '80801113':
        msg = 'RAM GDDR6 1 2 5'
    elif err_code[0:8] == '80801114':
        msg = 'RAM GDDR6 3 5'
    elif err_code[0:8] == '80801115':
        msg = 'RAM GDDR6 1 3 5'
    elif err_code[0:8] == '80801116':
        msg = 'RAM GDDR6 2 3 5'
    elif err_code[0:8] == '80801117':
        msg = 'RAM GDDR6 1 2 3 5'
    elif err_code[0:8] == '80801118':
        msg = 'RAM GDDR6 4 5'
    elif err_code[0:8] == '80801119':
        msg = 'RAM GDDR6 1 4 5'
    elif err_code[0:8] == '8080111A':
        msg = 'RAM GDDR6 2 4 5'
    elif err_code[0:8] == '8080111B':
        msg = 'RAM GDDR6 1 2 4 5'
    elif err_code[0:8] == '8080111C':
        msg = 'RAM GDDR6 3 4 5'
    elif err_code[0:8] == '8080111D':
        msg = 'RAM GDDR6 1 3 4 5'
    elif err_code[0:8] == '8080111E':
        msg = 'RAM GDDR6 2 3 4 5'
    elif err_code[0:8] == '8080111F':
        msg = 'RAM GDDR6 1 2 3 4 5'
    elif err_code[0:4] == '8080':
        msg = 'Fatal_OFF by BigOs - Failed to Start OS Kernel'
    elif err_code[0:4] == '8083':
        msg = 'SoC Sync Flood  Check PG2         '
    elif err_code[0:4] == 'B008':
        msg = 'Rebuild DBI Fail'
    return msg

def pw_state(pw_state):
    msg1 = '        '
    if pw_state[2:4] == '00':
        msg1 = 'SysReady:'
    elif pw_state[2:4] == '01':
        msg1 = 'MaOnStby:'
    elif pw_state[2:3] == '0':
        msg1 = 'Reserved:'
    elif pw_state[2:3] == '1':
        msg1 = 'PSP_____:'
    elif pw_state[2:4] == '20':
        msg1 = 'BIOS____:'
    elif pw_state[2:4] == '30':
        msg1 = 'BIOS____:'
    elif pw_state[2:4] == '40':
        msg1 = 'EAP_Redy:'
    elif pw_state[2:3] == '4':
        msg1 = 'EAP_____:'
    elif pw_state[2:3] == '5':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == '6':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == '7':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == '8':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == '9':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == 'A':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == 'B':
        msg1 = 'Kernel__:'
    elif pw_state[2:3] == 'C':
        msg1 = 'IntPrcss:'
    elif pw_state[2:3] == 'D':
        msg1 = 'IntPrcss:'
    elif pw_state[2:3] == 'E':
        msg1 = 'IntPrcss:'
    elif pw_state[2:4] == 'FF':
        msg1 = 'HstOsOFF:'
    elif pw_state[2:3] == 'F':
        msg1 = 'IntPrcss:'
    msg2 = '______'
    if pw_state[6:8] == '00':
        msg2 = 'ACIN_L'
    elif pw_state[6:8] == '01':
        msg2 = 'Stanby'
    elif pw_state[6:8] == '02':
        msg2 = 'PG2_ON'
    elif pw_state[6:8] == '03':
        msg2 = 'EFC_ON'
    elif pw_state[6:8] == '04':
        msg2 = 'EAP_ON'
    elif pw_state[6:8] == '05':
        msg2 = 'SOC_ON'
    elif pw_state[6:8] == '06':
        msg2 = 'ErrDET'
    elif pw_state[6:8] == '07':
        msg2 = 'FtlErr'
    elif pw_state[6:8] == '08':
        msg2 = 'NvrBot'
    elif pw_state[6:8] == '09':
        msg2 = 'FrcOFF'
    elif pw_state[6:8] == '0A':
        msg2 = 'FofBTd'
    return msg1 + msg2

def upcause(BT_TRG):
    msg = '___'
    if BT_TRG[0:8] == '40000000':
        msg = 'URT'
    elif BT_TRG[0:8] == '00080000':
        msg = 'BT '
    elif BT_TRG[0:8] == '00040000':
        msg = 'CEC'
    elif BT_TRG[0:8] == '00020000':
        msg = 'EAP'
    elif BT_TRG[0:8] == '00010000':
        msg = 'SoC'
    elif BT_TRG[0:8] == '00000400':
        msg = 'EjectSwitch'
    elif BT_TRG[0:8] == '00000200':
        msg = 'DLd'
    elif BT_TRG[0:8] == '00000100':
        msg = 'PowerButton'
    elif BT_TRG[0:8] == '00000001':
        msg = 'BPW'
    elif BT_TRG[0:8] == '00000000':
        msg = 'None / Unknown / Devkit'
    return msg

def psq(PSQ):
    msg = '_ _ _ _'
    if PSQ[0:4] == '2002':
        msg = 'EmcBootup'
    elif PSQ[0:4] == '2067':
        msg = 'EmcBootup'
    elif PSQ[0:4] == '2064':
        msg = '[EmcBootup  ,  FATAL OFF]'
    elif PSQ[0:4] == '218E':
        msg = 'EmcBootup'
    elif PSQ[0:4] == '2003':
        msg = 'Subsystem Peripheral Initialize'
    elif PSQ[0:4] == '2005':
        msg = 'Subsystem Peripheral Initialize'
    elif PSQ[0:4] == '2004':
        msg = 'Subsystem Peripheral Initialize'
    elif PSQ[0:4] == '2008':
        msg = 'aEmcTimerIniti'
    elif PSQ[0:4] == '2009':
        msg = 'aEmcTimerIniti'
    elif PSQ[0:4] == '200A':
        msg = 'aEmcTimerIniti'
    elif PSQ[0:4] == '200B':
        msg = 'aEmcTimerIniti'
    elif PSQ[0:4] == '200C':
        msg = 'aPowerGroup2On 1'
    elif PSQ[0:4] == '2109':
        msg = 'aPowerGroup2On 1'
    elif PSQ[0:4] == '200D':
        msg = 'aPowerGroup2On 1'
    elif PSQ[0:4] == '2011':
        msg = 'aPowerGroup2On 1'
    elif PSQ[0:4] == '200E':
        msg = '[aPowerGroup2On 1  ,  Subsystem PG2 reset]'
    elif PSQ[0:4] == '200F':
        msg = 'aPowerGroup2On 1'
    elif PSQ[0:4] == '2010':
        msg = '[aPowerGroup2On 1  ,  Subsystem PG2 reset  ,  Subsystem PG2 reset without PCIePLL]'
    elif PSQ[0:4] == '202E':
        msg = '[aPowerGroup2On 1  ,  Subsystem PG2 reset  ,  Subsystem PG2 reset without PCIePLL]'
    elif PSQ[0:4] == '2006':
        msg = '[aPowerGroup2On 1  ,  Subsystem PG2 reset  ,  Subsystem PG2 reset without PCIePLL]'
    elif PSQ[0:4] == '21AF':
        msg = 'aPowerGroup2On 1'
    elif PSQ[0:4] == '21B1':
        msg = 'aPowerGroup2On 1'
    elif PSQ[0:4] == '2014':
        msg = '[aPowerGroup2Off  ,  Flash Controller OFF EFC  ,  Flash Controller OFF EAP  ,  Flash Controller STOP EFC  ,  Flash Controller STOP EAP  ,  FATAL OFF]'
    elif PSQ[0:4] == '202F':
        msg = '[aPowerGroup2Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2015':
        msg = '[aPowerGroup2Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2016':
        msg = '[aPowerGroup2Off  ,  Subsystem PG2 reset  ,  FATAL OFF]'
    elif PSQ[0:4] == '202B':
        msg = '[aPowerGroup2Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2017':
        msg = '[aPowerGroup2Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '210A':
        msg = '[aPowerGroup2Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2018':
        msg = '[aPowerGroup2Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2019':
        msg = 'aPowerGroup2Off'
    elif PSQ[0:4] == '201A':
        msg = 'aSbPcieInitiali'
    elif PSQ[0:4] == '2030':
        msg = '[aSbPcieInitiali  ,  aSbPcieInitiali 1]'
    elif PSQ[0:4] == '2031':
        msg = '[aSbPcieInitiali  ,  aSbPcieInitiali 1]'
    elif PSQ[0:4] == '2066':
        msg = 'aSbPcieInitiali 1'
    elif PSQ[0:4] == '208D':
        msg = '[aEfcBootModeSet  ,  EAP Boot Mode Set]'
    elif PSQ[0:4] == '210B':
        msg = '[aEfcBootModeSet  ,  EAP Boot Mode Set]'
    elif PSQ[0:4] == '210C':
        msg = '[aEfcBootModeSet  ,  EAP Boot Mode Set]'
    elif PSQ[0:4] == '210D':
        msg = 'aEfcBootModeSet'
    elif PSQ[0:4] == '201D':
        msg = '[Flash Controller ON EFC  ,  Flash Controller ON EAP]'
    elif PSQ[0:4] == '2027':
        msg = '[Flash Controller ON EFC  ,  Flash Controller ON EAP  ,  Flash Controller Soft reset]'
    elif PSQ[0:4] == '2110':
        msg = '[Flash Controller ON EFC  ,  Flash Controller ON EAP]'
    elif PSQ[0:4] == '2033':
        msg = '[Flash Controller ON EFC  ,  Flash Controller ON EAP  ,  Flash Controller Soft reset]'
    elif PSQ[0:4] == '2089':
        msg = '[Flash Controller ON EFC  ,  Flash Controller ON EAP  ,  Flash Controller Soft reset]'
    elif PSQ[0:4] == '2035':
        msg = '[Flash Controller ON EFC  ,  Flash Controller ON EAP  ,  Flash Controller Soft reset  ,  FC NAND Close  Not urgent  ,  FC NAND Close  Urgent]'
    elif PSQ[0:4] == '2032':
        msg = 'Flash Controller Soft reset'
    elif PSQ[0:4] == '201C':
        msg = 'Subsystem PCIe USP Enable'
    elif PSQ[0:4] == '2029':
        msg = '[Subsystem PCIe DSP Enable  ,  Subsystem PCIe DSP Enable BT DL]'
    elif PSQ[0:4] == '2107':
        msg = '[Subsystem PCIe DSP Enable  ,  Dev WLAN BT PCIE RESET NEGATE  ,  Dev WLAN BT PCIE RESET ASSERT NEGATE]'
    elif PSQ[0:4] == '2159':
        msg = '[Flash Controller Initialization EFC  ,  Flash Controller Initialization EAP]'
    elif PSQ[0:4] == '2045':
        msg = '[Flash Controller Initialization EFC  ,  Flash Controller Initialization EAP]'
    elif PSQ[0:4] == '2038':
        msg = 'Flash Controller Initialization EFC'
    elif PSQ[0:4] == '2043':
        msg = '[Flash Controller Initialization EFC  ,  Flash Controller Initialization EAP]'
    elif PSQ[0:4] == '2041':
        msg = '[Flash Controller Initialization EFC  ,  Flash Controller Initialization EAP]'
    elif PSQ[0:4] == '2047':
        msg = 'Flash Controller Initialization EAP'
    elif PSQ[0:4] == '204C':
        msg = '[Flash Controller OFF EFC  ,  Flash Controller STOP EFC]'
    elif PSQ[0:4] == '2108':
        msg = '[Flash Controller OFF EFC  ,  Flash Controller OFF EAP  ,  Flash Controller STOP EFC  ,  Flash Controller STOP EAP  ,  FATAL OFF  ,  Dev WLAN BT PCIE RESET ASSERT  ,  Dev WLAN BT PCIE RESET ASSERT NEGATE]'
    elif PSQ[0:4] == '206D':
        msg = '[Flash Controller OFF EFC  ,  Flash Controller OFF EAP  ,  Flash Controller STOP EFC  ,  Flash Controller STOP EAP  ,  FATAL OFF]'
    elif PSQ[0:4] == '2034':
        msg = '[Flash Controller OFF EFC  ,  Flash Controller OFF EAP  ,  FATAL OFF]'
    elif PSQ[0:4] == '208A':
        msg = '[Flash Controller OFF EFC  ,  Flash Controller OFF EAP  ,  FATAL OFF]'
    elif PSQ[0:4] == '210F':
        msg = '[Flash Controller OFF EFC  ,  Flash Controller OFF EAP  ,  FATAL OFF]'
    elif PSQ[0:4] == '2028':
        msg = '[Flash Controller OFF EFC  ,  Flash Controller OFF EAP  ,  Flash Controller STOP EFC  ,  Flash Controller STOP EAP  ,  FATAL OFF]'
    elif PSQ[0:4] == '201E':
        msg = '[Flash Controller OFF EFC  ,  Flash Controller OFF EAP  ,  FATAL OFF]'
    elif PSQ[0:4] == '2046':
        msg = '[Flash Controller OFF EAP  ,  Flash Controller STOP EFC  ,  Flash Controller STOP EAP]'
    elif PSQ[0:4] == '2048':
        msg = '[Flash Controller STOP EFC  ,  Flash Controller STOP EAP]'
    elif PSQ[0:4] == '204D':
        msg = 'Flash Controller STOP EAP'
    elif PSQ[0:4] == '2049':
        msg = 'Flash Controller SRAM Keep Enable'
    elif PSQ[0:4] == '2111':
        msg = 'ACDC  ON'
    elif PSQ[0:4] == '2113':
        msg = 'ACDC  ON'
    elif PSQ[0:4] == '2052':
        msg = '[ACDC  ON  ,  FAN Control Start]'
    elif PSQ[0:4] == '2085':
        msg = '[ACDC  ON  ,  FAN Control Start]'
    elif PSQ[0:4] == '2054':
        msg = '[ACDC  ON  ,  FAN Control Start]'
    elif PSQ[0:4] == '2087':
        msg = '[ACDC  ON  ,  FAN Control Start]'
    elif PSQ[0:4] == '216F':
        msg = '[USB VBUS On  ,  USB VBUS Off  ,  Dev USB VBUS On]'
    elif PSQ[0:4] == '211B':
        msg = '[USB VBUS On  ,  Dev USB VBUS On]'
    elif PSQ[0:4] == '211D':
        msg = '[BD Drive Power On  ,  Dev BD Drive Power On]'
    elif PSQ[0:4] == '203A':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '203D':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2126':
        msg = '[Main SoC Power ON  Cold Boot  ,  FATAL OFF  ,  Main SoC PGA Power Off]'
    elif PSQ[0:4] == '2128':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit  ,  aWlan 1]'
    elif PSQ[0:4] == '212A':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit  ,  aWlan 1]'
    elif PSQ[0:4] == '2135':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit  ,  Main SoC Power Off  ,  FATAL OFF  ,  Dev VBURN OFF]'
    elif PSQ[0:4] == '211F':
        msg = '[Main SoC Power ON  Cold Boot  ,  GDDR6 USB Power On]'
    elif PSQ[0:4] == '2189':
        msg = '[Main SoC Power ON  Cold Boot  ,  GDDR6 USB Power On]'
    elif PSQ[0:4] == '218B':
        msg = '[Main SoC Power ON  Cold Boot  ,  GDDR6 USB Power On]'
    elif PSQ[0:4] == '21B6':
        msg = '[Main SoC Power ON  Cold Boot  ,  GDDR6 USB Power On]'
    elif PSQ[0:4] == '21B8':
        msg = '[Main SoC Power ON  Cold Boot  ,  GDDR6 USB Power On]'
    elif PSQ[0:4] == '21BA':
        msg = '[Main SoC Power ON  Cold Boot  ,  GDDR6 USB Power On]'
    elif PSQ[0:4] == '2023':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2125':
        msg = '[Main SoC Power ON  Cold Boot  ,  GDDR6 USB Power On]'
    elif PSQ[0:4] == '2167':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '21C1':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '21C3':
        msg = 'Main SoC Power ON  Cold Boot'
    elif PSQ[0:4] == '2121':
        msg = 'Main SoC Power ON  Cold Boot'
    elif PSQ[0:4] == '21C5':
        msg = 'Main SoC Power ON  Cold Boot'
    elif PSQ[0:4] == '2175':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2133':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2141':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '205F':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '218D':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '21BE':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '21C0':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '21C4':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2123':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2136':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2137':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '216D':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2060':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2061':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2025':
        msg = '[Main SoC Power ON  Cold Boot  ,  Main SoC Power ON  S3 Eit]'
    elif PSQ[0:4] == '2127':
        msg = '[Main SoC Reset Release  ,  Reset SoC  ,  Cold reset WA]'
    elif PSQ[0:4] == '204A':
        msg = 'Main SoC Reset Release'
    elif PSQ[0:4] == '2129':
        msg = '[Main SoC Reset Release  ,  Reset SoC  ,  Cold reset WA]'
    elif PSQ[0:4] == '21A3':
        msg = '[Main SoC Reset Release  ,  USB VBUS On 2  ,  Dev USBA1 VBUS On]'
    elif PSQ[0:4] == '21A5':
        msg = '[Main SoC Reset Release  ,  USB VBUS On 2  ,  Dev USBA2 VBUS On]'
    elif PSQ[0:4] == '21A7':
        msg = '[Main SoC Reset Release  ,  USB VBUS On 2  ,  Dev USBA3 VBUS On]'
    elif PSQ[0:4] == '21A9':
        msg = '[Main SoC Reset Release  ,  USB VBUS On 2  ,  Dev USBA1 VBUS On]'
    elif PSQ[0:4] == '21AB':
        msg = '[Main SoC Reset Release  ,  USB VBUS On 2  ,  Dev USBA2 VBUS On]'
    elif PSQ[0:4] == '21AD':
        msg = '[Main SoC Reset Release  ,  USB VBUS On 2  ,  Dev USBA3 VBUS On]'
    elif PSQ[0:4] == '212F':
        msg = '[Main SoC Reset Release  ,  Reset SoC]'
    elif PSQ[0:4] == '2169':
        msg = 'Main SoC Reset Release'
    elif PSQ[0:4] == '2161':
        msg = 'Main SoC Reset Release'
    elif PSQ[0:4] == '21B3':
        msg = 'Main SoC Reset Release'
    elif PSQ[0:4] == '21B5':
        msg = 'Main SoC Reset Release'
    elif PSQ[0:4] == '213C':
        msg = '[Main SoC Reset Release  ,  Reset SoC  ,  Cold reset WA]'
    elif PSQ[0:4] == '213D':
        msg = '[Main SoC Reset Release  ,  Reset SoC  ,  Cold reset WA]'
    elif PSQ[0:4] == '213F':
        msg = '[Main SoC Reset Release  ,  Reset SoC  ,  Cold reset WA]'
    elif PSQ[0:4] == '2050':
        msg = '[Main SoC Reset Release  ,  Reset SoC  ,  Cold reset WA]'
    elif PSQ[0:4] == '2083':
        msg = '[Main SoC Reset Release  ,  Reset SoC]'
    elif PSQ[0:4] == '2187':
        msg = 'Main SoC Reset Release'
    elif PSQ[0:4] == '2195':
        msg = 'Main SoC Reset Release'
    elif PSQ[0:4] == '2197':
        msg = 'Main SoC Reset Release'
    elif PSQ[0:4] == '2155':
        msg = '[Main SoC Reset Release  ,  Reset SoC]'
    elif PSQ[0:4] == '205C':
        msg = '[Main SoC Reset Release  ,  Reset SoC  ,  Cold reset WA]'
    elif PSQ[0:4] == '217F':
        msg = '[Main SoC Reset Release  ,  Cold reset WA]'
    elif PSQ[0:4] == '212B':
        msg = 'MSOC Reset Moni High'
    elif PSQ[0:4] == '2157':
        msg = 'MSOC Reset Moni High'
    elif PSQ[0:4] == '208F':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2040':
        msg = '[Main SoC Power Off  ,  FC NAND Close  Not urgent]'
    elif PSQ[0:4] == '2156':
        msg = '[Main SoC Power Off  ,  FATAL OFF  ,  aWlan 1]'
    elif PSQ[0:4] == '2196':
        msg = '[Main SoC Power Off  ,  Main SoC Thermal Moni Stop]'
    elif PSQ[0:4] == '2198':
        msg = '[Main SoC Power Off  ,  Main SoC Thermal Moni Stop]'
    elif PSQ[0:4] == '2188':
        msg = '[Main SoC Power Off  ,  Main SoC Thermal Moni Stop]'
    elif PSQ[0:4] == '2084':
        msg = '[Main SoC Power Off  ,  Main SoC Thermal Moni Stop  ,  aWlan 1]'
    elif PSQ[0:4] == '2051':
        msg = '[Main SoC Power Off  ,  Main SoC Thermal Moni Stop  ,  aWlan 1  ,  Cold reset WA]'
    elif PSQ[0:4] == '213E':
        msg = '[Main SoC Power Off  ,  FATAL OFF  ,  aWlan 1  ,  Cold reset WA]'
    elif PSQ[0:4] == '2140':
        msg = '[Main SoC Power Off  ,  FATAL OFF  ,  aWlan 1  ,  Cold reset WA]'
    elif PSQ[0:4] == '2162':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '216A':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '21B4':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2130':
        msg = '[Main SoC Power Off  ,  FATAL OFF  ,  aWlan 1]'
    elif PSQ[0:4] == '217D':
        msg = '[Main SoC Power Off  ,  FATAL OFF  ,  Cold reset WA]'
    elif PSQ[0:4] == '206C':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '215E':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2026':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2138':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2139':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2142':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '21BF':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '21C2':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2168':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2124':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2176':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '212C':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2158':
        msg = '[Main SoC Power Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '205D':
        msg = '[Main SoC Power Off  ,  EAP Reset Moni Assert]'
    elif PSQ[0:4] == '213B':
        msg = '[Main SoC Power Off  ,  EAP Reset Moni Assert]'
    elif PSQ[0:4] == '211E':
        msg = '[BD Drive Power Off  ,  FATAL OFF  ,  Dev BD Drive Power Off]'
    elif PSQ[0:4] == '211C':
        msg = '[USB VBUS Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2114':
        msg = '[ACDC  Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '2112':
        msg = '[ACDC  Off  ,  FATAL OFF]'
    elif PSQ[0:4] == '207A':
        msg = 'ACDC  Off'
    elif PSQ[0:4] == '2086':
        msg = '[ACDC  Off  ,  FATAL OFF  ,  FAN Control Stop]'
    elif PSQ[0:4] == '2053':
        msg = '[ACDC  Off  ,  FATAL OFF  ,  FAN Control Stop]'
    elif PSQ[0:4] == '2088':
        msg = '[ACDC  Off  ,  FATAL OFF  ,  FAN Control Stop]'
    elif PSQ[0:4] == '2055':
        msg = '[ACDC  Off  ,  FATAL OFF  ,  FAN Control Stop]'
    elif PSQ[0:4] == '204B':
        msg = '[FC NAND Close  Not urgent  ,  FC NAND Close  Urgent  ,  FATAL OFF  ,  Flash Controller STOP pre operation]'
    elif PSQ[0:4] == '2042':
        msg = '[FC NAND Close  Not urgent  ,  FC NAND Close  Urgent  ,  Flash Controller STOP pre operation]'
    elif PSQ[0:4] == '2044':
        msg = '[FC NAND Close  Not urgent  ,  FC NAND Close  Urgent  ,  Flash Controller STOP pre operation]'
    elif PSQ[0:4] == '212E':
        msg = '[FATAL OFF  ,  EAP Reset Moni Assert]'
    elif PSQ[0:4] == '2024':
        msg = '[FATAL OFF  ,  Stop NoSS Clock For Main SoC]'
    elif PSQ[0:4] == '2152':
        msg = '[FATAL OFF  ,  USB OC Moni de assert]'
    elif PSQ[0:4] == '2122':
        msg = '[FATAL OFF  ,  Main SoC PGB Power Off GDDR6 Power Off]'
    elif PSQ[0:4] == '21AA':
        msg = '[FATAL OFF  ,  USB OC Moni de assert 2  ,  Dev USBA1 VBUS Off]'
    elif PSQ[0:4] == '21AC':
        msg = '[FATAL OFF  ,  USB OC Moni de assert 2  ,  Dev USBA2 VBUS Off]'
    elif PSQ[0:4] == '21AE':
        msg = '[FATAL OFF  ,  USB OC Moni de assert 2  ,  Dev USBA3 VBUS Off]'
    elif PSQ[0:4] == '21A4':
        msg = '[FATAL OFF  ,  USB VBUS Off 2  ,  Dev USBA1 VBUS Off]'
    elif PSQ[0:4] == '21A6':
        msg = '[FATAL OFF  ,  USB VBUS Off 2  ,  Dev USBA2 VBUS Off]'
    elif PSQ[0:4] == '21A8':
        msg = '[FATAL OFF  ,  USB VBUS Off 2  ,  Dev USBA3 VBUS Off]'
    elif PSQ[0:4] == '21B7':
        msg = '[FATAL OFF  ,  Main SoC PGA Power Off]'
    elif PSQ[0:4] == '21B9':
        msg = '[FATAL OFF  ,  Main SoC PGA Power Off]'
    elif PSQ[0:4] == '21BB':
        msg = '[FATAL OFF  ,  Main SoC PGA Power Off]'
    elif PSQ[0:4] == '218C':
        msg = '[FATAL OFF  ,  Main SoC PGA Power Off]'
    elif PSQ[0:4] == '218A':
        msg = '[FATAL OFF  ,  Main SoC PGA Power Off]'
    elif PSQ[0:4] == '2120':
        msg = '[FATAL OFF  ,  Main SoC PGA Power Off]'
    elif PSQ[0:4] == '2118':
        msg = '[FATAL OFF  ,  HDMI5VOff  ,  Dev HDMI5V Power Off]'
    elif PSQ[0:4] == '2073':
        msg = '[FATAL OFF  ,  HDMI CECStop]'
    elif PSQ[0:4] == '2075':
        msg = '[FATAL OFF  ,  HDMI CECStop  ,  HDMIStop]'
    elif PSQ[0:4] == '2079':
        msg = '[FATAL OFF  ,  HDMI CECStop]'
    elif PSQ[0:4] == '2071':
        msg = '[FATAL OFF  ,  HDMI CECStop]'
    elif PSQ[0:4] == '204F':
        msg = '[FATAL OFF  ,  HDMI CECStop]'
    elif PSQ[0:4] == '2022':
        msg = '[FATAL OFF  ,  HDMI CECStop]'
    elif PSQ[0:4] == '2116':
        msg = '[FATAL OFF  ,  HDMI CECStop]'
    elif PSQ[0:4] == '208C':
        msg = '[FATAL OFF  ,  Floyd Reset Assert]'
    elif PSQ[0:4] == '2165':
        msg = '[FATAL OFF  ,  Floyd Reset Assert]'
    elif PSQ[0:4] == '201B':
        msg = '[FATAL OFF  ,  Stop PCIePLL SS NOSS part]'
    elif PSQ[0:4] == '208E':
        msg = '[FATAL OFF  ,  Titania2 GPIO Glitch Issue WA]'
    elif PSQ[0:4] == '2174':
        msg = '[FATAL OFF  ,  GPI SW Close]'
    elif PSQ[0:4] == '2164':
        msg = '[FATAL OFF  ,  PD USB I2C Close]'
    elif PSQ[0:4] == '216C':
        msg = '[FATAL OFF  ,  PD USB I2C Close]'
    elif PSQ[0:4] == '21B2':
        msg = '[FATAL OFF  ,  PD USB I2C Close]'
    elif PSQ[0:4] == '21B0':
        msg = '[FATAL OFF  ,  PD USB I2C Close]'
    elif PSQ[0:4] == '2012':
        msg = '[FATAL OFF  ,  Stop SFlash DMA]'
    elif PSQ[0:4] == '2091':
        msg = '[FATAL OFF  ,  FAN Control Stop  ,  Local Temp.3 OFF]'
    elif PSQ[0:4] == '2057':
        msg = '[FATAL OFF  ,  FAN Control Stop  ,  Local Temp.3 OFF]'
    elif PSQ[0:4] == '2192':
        msg = '[FATAL OFF  ,  FAN Control Stop]'
    elif PSQ[0:4] == '2190':
        msg = '[FATAL OFF  ,  FAN Control Stop]'
    elif PSQ[0:4] == '217E':
        msg = '[FATAL OFF  ,  Fan Servo Parameter Reset]'
    elif PSQ[0:4] == '2105':
        msg = '[FATAL OFF  ,  WLAN Module Reset  ,  WM Reset  ,  Dev WLAN BT RESET ASSERT  ,  Dev WLAN BT RESET ASSERT NEGATE]'
    elif PSQ[0:4] == '2092':
        msg = 'FATAL OFF'
    elif PSQ[0:4] == '210E':
        msg = 'EAP Boot Mode Set'
    elif PSQ[0:4] == '212D':
        msg = 'EAP Reset Moni de assert'
    elif PSQ[0:4] == '205E':
        msg = 'FAN CONTROL Parameter Reset'
    elif PSQ[0:4] == '2065':
        msg = 'EMC SoC Handshake  STR'
    elif PSQ[0:4] == '2151':
        msg = 'USB OC Moni Assert'
    elif PSQ[0:4] == '2068':
        msg = '[HDMI Standby  ,  HDMIStop  ,  CECStart]'
    elif PSQ[0:4] == '2106':
        msg = '[WLAN Module USB Enable  ,  WLAN Module Reset  ,  WM Reset  ,  Dev WLAN BT RESET NEGATE  ,  Dev WLAN BT RESET ASSERT NEGATE]'
    elif PSQ[0:4] == '217B':
        msg = '[WLAN Module Reset  ,  BT WAKE Disabled  ,  WM Reset  ,  Dev WLAN BT RESET ASSERT  ,  Dev WLAN BT RESET ASSERT NEGATE]'
    elif PSQ[0:4] == '2069':
        msg = '[WLAN Module Reset  ,  WM Reset  ,  Dev WLAN BT RESET ASSERT  ,  Dev WLAN BT RESET ASSERT NEGATE  ,  Dev WLAN BT PCIE RESET ASSERT  ,  Dev WLAN BT PCIE RESET ASSERT NEGATE]'
    elif PSQ[0:4] == '215A':
        msg = '1GbE NIC Reset de assert'
    elif PSQ[0:4] == '215B':
        msg = '1GbE NIC Reset assert'
    elif PSQ[0:4] == '2115':
        msg = '[HDMI CECStart  ,  CECStart]'
    elif PSQ[0:4] == '2021':
        msg = '[HDMI CECStart  ,  CECStart]'
    elif PSQ[0:4] == '204E':
        msg = '[HDMI CECStart  ,  CECStart]'
    elif PSQ[0:4] == '2070':
        msg = '[HDMI CECStart  ,  CECStart]'
    elif PSQ[0:4] == '2078':
        msg = '[HDMI CECStart  ,  CECStart]'
    elif PSQ[0:4] == '206E':
        msg = '[HDMI CECStart  ,  HDMI CECStart]'
    elif PSQ[0:4] == '2074':
        msg = '[HDMI CECStart  ,  HDMI CECStart]'
    elif PSQ[0:4] == '2072':
        msg = '[HDMI CECStart  ,  CECStart]'
    elif PSQ[0:4] == '2077':
        msg = 'HDMIStop'
    elif PSQ[0:4] == '2076':
        msg = 'InActiveSource Send'
    elif PSQ[0:4] == '2117':
        msg = '[HDMI5VOn  ,  Dev HDMI_5V Power On]'
    elif PSQ[0:4] == '206F':
        msg = 'HDMI CECInit'
    elif PSQ[0:4] == '207B':
        msg = 'GDDR6 NAND Voltage Setting'
    elif PSQ[0:4] == '207C':
        msg = 'GDDR6 NAND Voltage Setting'
    elif PSQ[0:4] == '207D':
        msg = 'GDDR6 NAND Voltage Setting'
    elif PSQ[0:4] == '215C':
        msg = 'PCIe Redriver EQ Setting'
    elif PSQ[0:4] == '2093':
        msg = 'Main SoC PGB Power Off GDDR6 Power Off'
    elif PSQ[0:4] == '2080':
        msg = 'Subsystem PG2 reset without PCIePLL'
    elif PSQ[0:4] == '2081':
        msg = 'Subsystem PG2 reset without PCIePLL'
    elif PSQ[0:4] == '216B':
        msg = 'PD USB I2C Open'
    elif PSQ[0:4] == '2163':
        msg = 'PD USB I2C Open'
    elif PSQ[0:4] == '2166':
        msg = 'Floyd Reset De assert'
    elif PSQ[0:4] == '208B':
        msg = 'Floyd Reset De assert'
    elif PSQ[0:4] == '2056':
        msg = '[FAN Control Start  ,  Local Temp.3 ON]'
    elif PSQ[0:4] == '2090':
        msg = '[FAN Control Start  ,  Local Temp.3 ON]'
    elif PSQ[0:4] == '218F':
        msg = 'FAN Control Start'
    elif PSQ[0:4] == '2191':
        msg = 'FAN Control Start'
    elif PSQ[0:4] == '215F':
        msg = 'MDCDC ON'
    elif PSQ[0:4] == '2160':
        msg = 'MDCDC Off'
    elif PSQ[0:4] == '216E':
        msg = 'Check AC IN DETECT'
    elif PSQ[0:4] == '2170':
        msg = 'Check BD DETECT'
    elif PSQ[0:4] == '2173':
        msg = 'GPI SW Open'
    elif PSQ[0:4] == '2102':
        msg = 'Devkit IO Epander Initialize'
    elif PSQ[0:4] == '2177':
        msg = 'Salina PMIC Register Initialize'
    elif PSQ[0:4] == '2178':
        msg = 'Disable AC IN DETECT'
    elif PSQ[0:4] == '2179':
        msg = 'BT WAKE Enabled'
    elif PSQ[0:4] == '2094':
        msg = 'Stop PCIePLL NoSS part'
    elif PSQ[0:4] == '217A':
        msg = 'Titania PMIC Register Initialize'
    elif PSQ[0:4] == '203B':
        msg = 'Setup FC for BTFW DL'
    elif PSQ[0:4] == '2039':
        msg = 'Setup FC for BTFW DL'
    elif PSQ[0:4] == '217C':
        msg = 'BTFW Download'
    elif PSQ[0:4] == '2095':
        msg = 'Telstar ROM Boot Wait'
    elif PSQ[0:4] == '2082':
        msg = 'Stop PCIePLL SS part'
    elif PSQ[0:4] == '2013':
        msg = 'Stop Subsystem PG2 Bus Error Detection(DDR4 BufferOverflow)'
    elif PSQ[0:4] == '2180':
        msg = 'FAN Control Start at Restmode during US'
    elif PSQ[0:4] == '2181':
        msg = 'FAN Control Start at Restmode during US'
    elif PSQ[0:4] == '2182':
        msg = 'FAN Control Start at Restmode during US'
    elif PSQ[0:4] == '2193':
        msg = 'FAN Control Start at Restmode during US'
    elif PSQ[0:4] == '2183':
        msg = 'FAN Control Stop at Restmode during USB'
    elif PSQ[0:4] == '2184':
        msg = 'FAN Control Stop at Restmode during USB'
    elif PSQ[0:4] == '2185':
        msg = 'FAN Control Stop at Restmode during USB'
    elif PSQ[0:4] == '2194':
        msg = 'FAN Control Stop at Restmode during USB'
    elif PSQ[0:4] == '2186':
        msg = 'Read Titania PMIC Register'
    elif PSQ[0:4] == '219B':
        msg = 'I2C Open'
    elif PSQ[0:4] == '219C':
        msg = 'I2C Open'
    elif PSQ[0:4] == '219D':
        msg = 'I2C Open'
    elif PSQ[0:4] == '219E':
        msg = 'I2C Open'
    elif PSQ[0:4] == '2199':
        msg = 'I2C Open'
    elif PSQ[0:4] == '219A':
        msg = 'I2C Open'
    elif PSQ[0:4] == '21A0':
        msg = 'Drive FAN Control Stop'
    elif PSQ[0:4] == '219F':
        msg = 'Drive FAN Control Stop'
    elif PSQ[0:4] == '21A1':
        msg = 'Drive FAN Control Start'
    elif PSQ[0:4] == '21A2':
        msg = 'Drive FAN Control Start'
    elif PSQ[0:4] == '2134':
        msg = 'Dev VBURN ON'
    return msg

def devpower(devpower_hex):
    value = int(devpower_hex, 16)
    result = ""

    h_on = (value & 0x10) != 0
    b_on = (value & 0x08) != 0
    c_on = (value & 0x04) != 0
    u_on = (value & 0x02) != 0
    w_on = (value & 0x01) != 0

    result += f"HDMI_5V: {'ON' if h_on else 'OFF'}, "
    result += f"BDD: {'ON' if b_on else 'OFF'}, "
    result += f"HDMI-CEC: {'ON' if c_on else 'OFF'}, "
    result += f"USB-VBUS: {'ON' if u_on else 'OFF'}, "
    result += f"WIFI: {'ON' if w_on else 'OFF'}"

    return result