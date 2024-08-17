import Fun
import NMFun
node_response = []
# 切换至创建隧道界面
def switch_create_tunnel(title_type, type):
    user_type = Fun.GetText('info', 'type')
    if type == 'VIP' and user_type == '普通用户':
        return Fun.MessageBox('您未拥有使用该类型隧道的权限', 'info', 'info')
    Fun.SetText('create', 'title_type', title_type)
    NMFun.get_node(type)
    Fun.SetEnable('create', 'name', True)
    Fun.SetVisible('create', 'edit', False)
    Fun.SetEnable('create', 'edit', False)
    Fun.SetVisible('create', 'delete', False)
    Fun.SetEnable('create', 'delete', False)
    Fun.SetVisible('create', 'create', True)
    info = ['name', 'local_ip', 'local_port', 'remote_port']
    for kj in info:
        Fun.SetText('create', kj, '')
    Fun.SelectPage('main', 'NoteBook_1', 2)
# 切换至编辑隧道界面
def switch_edit_tunnel(name, type, port):
    global node_response
    if name in NMFun.notified_tunnels or NMFun.notified_tunnels != []:
        Fun.MessageBox('请先关闭当前运行中的隧道', 'info', 'info')
        return
    server_url = NMFun.server_url
    Fun.SelectPage('main', 'NoteBook_1', 2)
    Fun.SetText('create', 'title_type', '编辑隧道')
    if not node_response:  # 如果节点列表为空或从未正确初始化，从服务器获取数据
        NMFun.fetch_node_data()
    for server in node_response:
        if type == server.get('name'):
            node_type = server.get('type')
            Fun.SetText('create', 'remote_ip', type)
    Fun.SetText('create', 'remote_port', port)
    Fun.SetText('create', 'name', name)
    Fun.SetText('create', 'local_ip', '')
    Fun.SetText('create', 'local_port', '')
    Fun.SetVisible('create', 'create', False)
    Fun.SetEnable('create', 'name', False)
    Fun.SetEnable('create', 'delete', True)
    Fun.SetVisible('create', 'delete', True)
    Fun.SetEnable('create', 'edit', True)
    Fun.SetVisible('create', 'edit', True)
