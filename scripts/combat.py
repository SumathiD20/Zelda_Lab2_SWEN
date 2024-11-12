using UnityEngine;
using System.Collections;

public class SparringNPC : MonoBehaviour
{
    public float attackRange = 2.0f;      // Range at which NPC can attack the player
    public float attackCooldown = 1.5f;   // Time between attacks
    public float moveSpeed = 2.0f;        // Movement speed of the NPC
    public float sparDamage = 5.0f;       // Reduced damage for sparring
    private bool isAttacking = false;     // State to prevent spamming attacks

    private Transform player;             // Reference to the player’s transform
    private Animator animator;            // Animator component to control animations

    void Start()
    {
        // Find the player and initialize components
        player = GameObject.FindWithTag("Player").transform;
        animator = GetComponent<Animator>();
    }

    void Update()
    {
        float distanceToPlayer = Vector3.Distance(player.position, transform.position);

        if (distanceToPlayer <= attackRange && !isAttacking)
        {
            StartCoroutine(AttackPlayer());
        }
        else if (distanceToPlayer > attackRange)
        {
            FollowPlayer();
        }
    }

    // Move towards the player if out of attack range
    void FollowPlayer()
    {
        animator.SetBool("IsWalking", true);
        Vector3 direction = (player.position - transform.position).normalized;
        transform.position += direction * moveSpeed * Time.deltaTime;
    }

    // Coroutine to handle attacking the player with cooldown
    IEnumerator AttackPlayer()
    {
        isAttacking = true;
        animator.SetTrigger("Attack");
        
        // Check if the player is still in range before applying damage
        yield return new WaitForSeconds(0.5f); // Delay for animation sync

        if (Vector3.Distance(player.position, transform.position) <= attackRange)
        {
            player.GetComponent<PlayerHealth>().TakeDamage(sparDamage);
        }

        yield return new WaitForSeconds(attackCooldown);
        isAttacking = false;
    }

    // Function for dodging the player's attack
    public void Dodge()
    {
        if (Random.value > 0.5f) // 50% chance to dodge
        {
            animator.SetTrigger("Dodge");
            // Logic to move the NPC out of the player's range briefly
        }
    }
