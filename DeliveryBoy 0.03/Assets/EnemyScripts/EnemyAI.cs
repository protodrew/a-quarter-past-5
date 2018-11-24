using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyAI : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}

/* Order of operations


    - Enemy 'sees' player (player comes into raycast)
    - Enemy moves within radius of player
    - Enemy opens fire while circling perimeter (randomly change direction)

*/