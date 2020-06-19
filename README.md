# Verilog Code Generator (VCG)

## 모든 내용은 가능하면 jupyter notebook에 정리하고자 합니다. 

## code_gen.ipynb 를 통해서 확인 부탁드립니다. 


code gen에서 표현이 필요한 경우의 수를 모두 정리해야 합니다. 

1. connect
    1. port
        - port-to-port
            - instance_port-to-instance_port
            - 
        - top-to-port
        - port-to-top
        - concat
        - replicate
    2. tie (ground 혹은 vcc와 직접 연결 되는 선)
        - port-to-GND
        - port-to-VCC
    4. bus 
        - various protocol

2. non-connect
    - only-port


```json
{
    "type" : "connect",
    "master" : {
        "
    }
}
```



