my_dict = {'1/2':
               {'-1/3': 'Strange Quark',
                '2/3': 'Charm Quark',
                '-1': 'Electron Lepton',
                '0': 'Muon Lepton'},
           '1': {'0': 'Photon Boson'}}

spin = input()
el_ch = input()
print(my_dict[spin][el_ch])
