#from Packets.Client.sraki import *; from Packets.Client.change_status import *; from Packets.Client.send_message import *; from Packets.Client.dm_message import *; from Packets.Client.file_upload import *; from Packets.Client.online import *; from Packets.Client.reactions import *;  
#from Packets.Server.get_dm import *; from Packets.Server.send_message import *; from Packets.Server.get_channels import *; from Packets.Server.get_message import *; from Packets.Server.get_servers import *; from Packets.Server.join_server import *; from Packets.Server.leave_server import *;

from design import *

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())