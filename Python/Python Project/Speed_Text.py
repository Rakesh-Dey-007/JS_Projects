# Network Speed Test --->

import speedtest

st = speedtest.Speedtest()

option = int(input('''What speed do you want to measure : 
                   1. Download Speed
                   2. Upload Speed
                   3. Ping
                   Enter Your Choice (1-3) : '''))

if option == 1:
    print(st.download()/(1025*1025),"Mbps")

elif option == 2:
    print(st.upload()/(1025*1025),"Mbps")

elif option == 3:
    print(st.results.ping,"ms")

else:
    print("Invalid Option")
