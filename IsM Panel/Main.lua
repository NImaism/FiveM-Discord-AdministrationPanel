datas = {}
CreateThread(function()
    while true do
        Wait(1000*2) 
        datas['File'] = LoadResourceFile(GetCurrentResourceName(), "./request.json") 
        if datas['File'] and json.decode(datas['File']) and json.decode(datas['File']) ~= datas['File'] then
            datas['File'] = json.decode(datas['File'])
        else
            datas['File'] = nil
        end
        if not datas['File'] then
            SaveResourceFile(GetCurrentResourceName(), 'request.json', json.encode({}))
            datas['File'] = {}
       end
       for _,i in pairs(datas['File']) do
          ExecuteCommand(i)
       end  
       SaveResourceFile(GetCurrentResourceName(), 'request.json', '{}')

    end
end)
